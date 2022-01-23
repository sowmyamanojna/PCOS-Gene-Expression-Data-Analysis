# Minimal Project
A  minimal theme for project pages.

Live Demo: [hugo-minimal-project/](https://sowmyamanojna.github.io/hugo-minimal-project/)  
Features: [code highlight](https://sowmyamanojna.github.io/hugo-minimal-project/#code-block-with-hugos-internal-highlight-shortcode), [inline math](https://sowmyamanojna.github.io/hugo-minimal-project/#math), [emojis :smile:](https://sowmyamanojna.github.io/hugo-minimal-project/#fun)

---

- Inspired by [Implicit Image Compression Project page](https://varun19299.github.io/implicit-image-compression/).  
- Based on [OneDly](https://github.com/cdeck3r/OneDly-Theme), [Hugo Book](https://github.com/alex-shpak/hugo-book) and [Wowchemy Academic](https://github.com/wowchemy/starter-academic).

---
#### Quick Start
1. Create a new site named quickstart
    ```
    hugo new site quickstart
    cd quickstart
    git init
    ```
2. Add the *minimal-project* theme
    ```
    git submodule add https://github.com/sowmyamanojna/hugo-minimal-project.git themes/minimal-project
    echo theme = \"minimal-project\" >> config.toml
    ```
3. [Optional: TLDR] In order to test how the site actually looks (real quick), copy the contents inside `exampleSite` to the main folder.
    ```
    cp -rf themes/minimal-project/exampleSite/* .
    ```
4. [Slow Customization] Start with copying the `config.toml` file and then customizing it.
    ```
    cp -rf themes/minimal-project/exampleSite/config.toml .
    cp -rf themes/minimal-project/exampleSite/static/* ./static
    ```

    Add files inside the `content/main` folder. As a sample, start with:
    ```
    +++
    title = "Content"
    description = "Initial project description"
    date = "2021-01-06"
    toc = true
    +++

    ## Hello World
    Hello there! Congratulations on getting the site up and running!  :tada:

    Start off with a brief description of the project here. :smile:
    ```

5. View your webpage
    ```
    hugo server
    ```

---
#### Customization
The images and files should be placed in the `static/` folder.

Options available:

- `proposal`: Boolean flag indicating the presence of a project proposal.
- `proposal_image`: Thumbnail image to be displayed (relative path).
- `proposal_file`: Link to the file (relative path).
- `midterm`: Boolean flag indicating the presence of a project midterm report.
- `midterm_image`: Thumbnail image to be displayed (relative path).
- `midterm_file`: Link to the file (relative path).
- `final`: Boolean flag indicating the presence of a project final report.
- `final_image`: Thumbnail image to be displayed (relative path).
- `final_file`: Link to the file (relative path).
- `demo`: Boolean flag indicating the presence of a project demo.
- `demo_image`: Thumbnail image to be displayed.
- `demo_url`: Link to a demo video (if any).
- `code`: Link to Code.
- `wandb`: Link to WandB project/report.

More options can be added. Modify the `intro.html` inside `theme/minimal-project/layout/partial/`.

