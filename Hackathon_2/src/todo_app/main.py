"""
Console Todo Application - Main Entry Point

This is the main entry point for the console todo application.
"""
from .cli.menu import TodoMenu


def main():
    """Main entry point for the application."""
    print("Welcome to the Console Todo Application!")
    menu = TodoMenu()
    menu.run()


if __name__ == "__main__":
    main()