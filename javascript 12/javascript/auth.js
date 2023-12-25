function authenticate() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    // Cek username dan password
    if (username === "nama-anda" && password === "student-nf23") {
        // Jika berhasil, arahkan ke halaman sukses
        window.location.href = "sukses.html";
    } else {
        // Jika gagal, tampilkan pesan error
        alert("Login gagal. Periksa kembali username dan password.");
    }
}
