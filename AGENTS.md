# AI Agent Instructions

Instructions for AI assistants working in this repository. This is the canonical source for all AI tools. Entry points: [CLAUDE.md](CLAUDE.md) (Claude), [.cursor/rules/agents.mdc](.cursor/rules/agents.mdc) (Cursor).

## Writing style

If an em-dash would normally appear, use a comma, hyphen, or period instead, even if it is not the perfect use of punctuation.

## Pull requests

When opening a pull request:

1. Follow [CONTRIBUTING.md](CONTRIBUTING.md) for branch naming, PR naming, and change requirements.
2. Use the PR title format: `type(guide-category): short detailed description` (example: `feat(sonarr): Update Why only WEB-DL FAQ with remux setup guidance`).
3. Fill out the full PR body using [.github/PULL_REQUEST_TEMPLATE.md](.github/PULL_REQUEST_TEMPLATE.md):
    - **Purpose**
    - **Approach**
    - **Open Questions and Pre-Merge TODOs**
    - **Requirements** (check both boxes when applicable)
4. Open as a **draft** if the work is incomplete or not ready for review.
5. Add an **AI disclosure** section at the end of the PR body:

```markdown
## AI disclosure

This pull request was created with AI assistance.
```

## GitHub issues

When opening a GitHub issue:

1. Follow repository policy in [.github/ISSUE_TEMPLATE/config.yml](.github/ISSUE_TEMPLATE/config.yml). Bug reports are normally confirmed on [Discord](https://trash-guides.info/discord) first and opened on GitHub by the team. Do not open bug issues directly unless a maintainer has asked you to.
2. If an issue is appropriate, use [.github/ISSUE_TEMPLATE/bug-error-found-in-the-guide.yml](.github/ISSUE_TEMPLATE/bug-error-found-in-the-guide.yml) and complete every required field.
3. Add an **AI disclosure** section at the end of the issue body:

```markdown
## AI disclosure

This issue was created with AI assistance.
```

## AI disclosure

Always disclose AI involvement in pull requests and GitHub issues opened on behalf of a user. Do not omit or obscure AI assistance.
