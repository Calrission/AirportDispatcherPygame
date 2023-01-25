from App import App

if __name__ == '__main__':
    app = App()

    while app.running:
        app.tick()
