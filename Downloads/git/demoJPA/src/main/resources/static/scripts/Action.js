function validatePassword() {
    var password = document.getElementById("password").value;
    var confirmPassword = document.getElementById("confirmPassword").value;

    if (password !== confirmPassword) {
        alert("Mật khẩu không khớp, vui lòng nhập lại!");
        return false; // Ngăn chặn form được gửi
    }
    return true; // Cho phép form được gửi
}
