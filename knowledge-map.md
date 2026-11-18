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
  brazil["Brazil"]
  architecture["Architecture"]
  web_history["Early Web History"]
  museums_and_galleries["Museums, Galleries and Art Media"]
  design_schools["Design Schools"]
  art_history["Art History and Artists"]
  egypt["Ancient Egypt"]
  ux_process["UX Design Process"]
  awards["Design Awards"]
  cinema["Cinema"]
  magazines["Magazines and Newspapers"]
  publishers["Publishers"]
  online_learning["Online Learning"]
  regions["Regions of the World"]
  design_systems["Design Systems"]
  design_to_code["Design to Code"]
  handoff["Developer Handoff"]
  research_and_testing["Research and Testing Tools"]
  metrics_and_growth["Metrics and Growth"]
  benchmarks["Benchmarks and Competitors"]
  ecommerce["E-commerce"]
  forms["Forms"]
  tables_and_dashboards["Tables and Dashboards"]
  data_visualization["Data Visualization"]
  email_design["Email Design"]
  writing["Writing and UX Writing"]
  accessibility["Accessibility and Inclusive Design"]
  mobile_design["Mobile Design"]
  ai_and_creative_tech["AI and Creative Technology"]
  english_for_designers["English for Designers"]
  product_management["Product Management"]
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
  motion --- cinema
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
  brazil --- portugal
  brazil --- regions
  brazil --- typography
  brazil --- architecture
  architecture --- graphic_design_history
  museums_and_galleries --- photo_archives
  museums_and_galleries --- graphic_design_history
  museums_and_galleries --- portugal
  museums_and_galleries --- design_schools
  design_schools --- learning
  design_schools --- portugal
  art_history --- museums_and_galleries
  art_history --- graphic_design_history
  art_history --- egypt
  egypt --- museums_and_galleries
  egypt --- rtl
  ux_process --- ux_research
  ux_process --- ux_curators
  ux_process --- online_learning
  awards --- web_galleries
  awards --- magazines
  awards --- regions
  cinema --- typography
  cinema --- regions
  magazines --- publishers
  magazines --- graphic_design_history
  publishers --- learning
  publishers --- art_history
  online_learning --- learning
  online_learning --- design_schools
  regions --- museums_and_galleries
  regions --- art_history
  design_systems --- component_libraries
  design_systems --- design_to_code
  design_systems --- motion
  design_to_code --- component_libraries
  design_to_code --- handoff
  handoff --- design_systems
  research_and_testing --- ux_research
  research_and_testing --- metrics_and_growth
  research_and_testing --- ux_process
  metrics_and_growth --- benchmarks
  metrics_and_growth --- ecommerce
  benchmarks --- ecommerce
  ecommerce --- ux_research
  ecommerce --- forms
  forms --- tables_and_dashboards
  forms --- accessibility
  forms --- writing
  tables_and_dashboards --- data_visualization
  tables_and_dashboards --- design_systems
  data_visualization --- graphic_design_history
  email_design --- writing
  email_design --- web_galleries
  writing --- english_for_designers
  accessibility --- design_systems
  accessibility --- mobile_design
  mobile_design --- ui_patterns
  mobile_design --- motion
  ai_and_creative_tech --- design_to_code
  ai_and_creative_tech --- motion
  ai_and_creative_tech --- tools
  english_for_designers --- learning
  product_management --- metrics_and_growth
  product_management --- research_and_testing
  product_management --- ux_process
```

## Open as an Obsidian Vault

1. Clone the repository.
2. In Obsidian choose Open folder as vault and pick the cloned folder.
3. Open Graph view: every topic file is a node, and the Related links are the edges.

Tags in each file's front matter (for example `history`, `portugal`, `rtl`) show up in the tag pane and can colour the graph.

## Planned Topics

- Personal library: books worth owning, with legal links
- Second pass on regions: Latin American, African and Asian graphic design
- Archive of saved Instagram posts with transcripts

[Back to the index](README.md)
