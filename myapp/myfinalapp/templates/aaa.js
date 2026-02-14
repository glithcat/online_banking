const checkbox = document.getElementById("new_account");
const newAccountField = document.getElementById("new_account_field");

checkbox.addEventListener("change", function() {
	newAccountField.style.display = this.checked ? 'block' : 'none';
})
