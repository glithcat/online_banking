const checkbox = document.getElementById("new_account");
const login_block = document.getElementById("login_block");
checkbox.addEventListener("change", function() {
login_block.style = this.checked ? 'login_block' : 'none';
