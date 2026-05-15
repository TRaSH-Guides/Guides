# Recommended Naming Scheme

**Settings → General → Naming.**

Bindery uses Go template syntax for naming. Two separate templates: one for ebooks, one for audiobooks.

---

## Ebook naming

### Folder

```
{Author Name}/{Book Title} ({Year})
```

### File

```
{Author Name} - {Book Title} ({Year}){Quality}
```

**Example:** `Brandon Sanderson - The Way of Kings (2010).epub`

If you store multiple formats per book, include quality to avoid collisions:

```
{Author Name} - {Book Title} ({Year}) [{Quality}]
```

**Example:** `Brandon Sanderson - The Way of Kings (2010) [EPUB].epub`

---

## Audiobook naming

### Folder

```
{Author Name}/{Book Title} ({Year})
```

For multi-disc releases where files land in subdirectories, the folder structure is preserved from the downloaded archive. Bindery does not flatten multi-part audiobooks.

### File

```
{Author Name} - {Book Title} ({Year}){Quality}
```

**Example:** `Brandon Sanderson - The Way of Kings (2010).m4b`

---

## Available tokens

| Token | Example output |
|---|---|
| `{Author Name}` | `Brandon Sanderson` |
| `{Author NameThe}` | `Sanderson, Brandon` |
| `{Book Title}` | `The Way of Kings` |
| `{Book TitleThe}` | `Way of Kings, The` |
| `{Series}` | `The Stormlight Archive` |
| `{Series Number}` | `1` |
| `{Year}` | `2010` |
| `{ISBN}` | `9780765326355` |
| `{Quality}` | `EPUB` |
| `{Quality Full}` | `EPUB Proper` |

Tokens that are empty for a given book (e.g. `{Series}` on a standalone) are silently dropped including any surrounding brackets or parentheses.

---

## Quality profiles

**Settings → Quality Profiles → Add.**

Bindery ranks formats internally by quality. Recommended ordering for ebooks:

```
EPUB > AZW3 > MOBI > PDF > CBZ/CBR
```

For audiobooks:

```
M4B > FLAC > MP3 320 > MP3 VBR > MP3 128 > AAC
```

Set size limits to avoid grabbing split-chapter uploads that are missing parts. A single-file M4B for a full novel is typically 200–600 MB; multi-file MP3 sets vary widely.

!!! tip "Usenet vs torrents"
    Set a higher **Priority** value on Usenet indexers (**Settings → Indexers**) if you want Bindery to prefer Usenet releases over torrents when both are available for the same book. Priority is a direct scoring bonus — a difference of 25–50 points is enough to consistently prefer one protocol without overriding quality differences.
