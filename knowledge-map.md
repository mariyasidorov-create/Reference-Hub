# Knowledge Map

How the topics connect. GitHub renders the diagram below; Obsidian builds the same graph automatically from the links between topic files.

```mermaid
graph LR
  ui_patterns["UI Patterns and Real Products"]
  web_galleries["Web Galleries"]
  images_and_moodboards["Images and Moodboards"]
  color["Color"]
  typography["Typography and Type Foundries"]
  motion["Motion and Micro-interactions"]
  ux_research["UX Research and Guidelines"]
  component_libraries["Component Libraries"]
  photo_archives["Photo and Image Archives"]
  portugal["Portugal"]
  awesome_lists["Claude Skills and Awesome Lists"]
  icons_and_graphics["Icons, Illustrations and Graphics"]
  tools["Tools"]
  off_topic["Off Topic"]
  learning["Learning"]
  graphic_design_history["Graphic Design History"]
  rtl["Right-to-Left Scripts"]
  architecture["Architecture"]
  web_history["Early Web History"]
  ux_curators["UX Curators and Vitaly Friedman"]
  ui_patterns --- web_galleries
  ui_patterns --- ux_research
  ui_patterns --- component_libraries
  web_galleries --- web_history
  web_galleries --- typography
  images_and_moodboards --- photo_archives
  images_and_moodboards --- icons_and_graphics
  images_and_moodboards --- color
  color --- typography
  typography --- graphic_design_history
  typography --- rtl
  typography --- portugal
  motion --- component_libraries
  ux_research --- ux_curators
  component_libraries --- awesome_lists
  photo_archives --- graphic_design_history
  photo_archives --- portugal
  portugal --- architecture
  portugal --- graphic_design_history
  awesome_lists --- tools
  icons_and_graphics --- tools
  tools --- motion
  off_topic --- learning
  learning --- graphic_design_history
  learning --- ux_curators
  graphic_design_history --- rtl
  graphic_design_history --- web_history
  architecture --- graphic_design_history
```

## Open as an Obsidian Vault

1. Clone the repository.
2. In Obsidian choose Open folder as vault and pick the cloned folder.
3. Open Graph view: every topic file is a node, and the Related links are the edges.

Tags in each file's front matter (for example `history`, `portugal`, `rtl`) show up in the tag pane and can colour the graph.

## Planned Topics

- Cinema and title design
- Regions: the Americas, Africa, Oceania, East and South-East Asia, Scotland
- Magazines and newspapers
- Publishers
- Museums
- Online courses
- Artists
- Design awards

[Back to the index](README.md)
