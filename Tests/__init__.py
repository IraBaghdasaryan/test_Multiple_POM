def with_(self, username, password):
    self._type(self._username_input, username)
    self._type(self._password_input, password)
    self._click(self._submit_button)