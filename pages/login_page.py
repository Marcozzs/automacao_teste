class LoginPage:
    def __init__(self, page):
        self.page = page
        # Seletores reais do Sauce Demo
        self.username_input = "#user-name"
        self.password_input = "#password"
        self.login_button = "#login-button"

    def login(self, user, password):
        self.page.fill(self.username_input, user)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)