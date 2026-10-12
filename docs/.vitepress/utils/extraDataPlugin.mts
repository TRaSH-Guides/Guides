import type MarkdownIt from "markdown-it";

const EXPR_RE = /\{\{\s*([a-zA-Z_][a-zA-Z0-9_]*(?:\[(?:'[^']*'|"[^"]*"|\d+)\])+)\s*\}\}/g;
const KEY_RE = /\[(?:'([^']*)'|"([^"]*)"|(\d+))\]/g;

function resolvePath(expr: string, data: Record<string, unknown>): string | undefined {
  const identMatch = expr.match(/^[a-zA-Z_][a-zA-Z0-9_]*/)!;
  // Only touch expressions rooted at a known docs/json namespace; anything else
  // (e.g. literal `{{ }}` placeholders inside included script files) is left as-is.
  if (!(identMatch[0] in data)) return undefined;
  let current: unknown = data[identMatch[0]];
  const rest = expr.slice(identMatch[0].length);
  KEY_RE.lastIndex = 0;
  let m: RegExpExecArray | null;
  while ((m = KEY_RE.exec(rest))) {
    if (current == null) break;
    const key = m[1] ?? m[2] ?? Number(m[3]);
    current = (current as Record<string | number, unknown>)[key];
  }
  if (current == null || typeof current === "object") {
    throw new Error(`extradata: could not resolve "{{ ${expr} }}"`);
  }
  return String(current);
}

/** Replaces markdownextradata-style `{{ namespace['key'][0] }}` expressions with
 * their resolved values from docs/json, before markdown-it/VitePress ever sees them. */
export function extraDataPlugin(md: MarkdownIt, data: Record<string, unknown>) {
  md.core.ruler.before("normalize", "extradata", (state) => {
    state.src = state.src.replace(EXPR_RE, (full, expr: string) => resolvePath(expr, data) ?? full);
  });
}
