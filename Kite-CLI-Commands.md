# Kite CLI commands:

### Initializing a Kite project:

- Once your working directory is you projects folder, or the folder you want your Kite project to go, type `kite build init (project name)`, into the terminal to create a Kite project structure.

### Removing a Kite project:

- First you need to be in your projects folder, then type `kite build remove (project name)`, into the terminal to delete your Kite project.

### Debug commands in Kite:

- `kite debug readlines (filename.ki)`, shows you what the compiler sees, in the terminal.
- `kite debug lexer (filename.ki)`, creates a `.txt` file in your `build/tokens` folder, containing the outputted tokens from the lexer.