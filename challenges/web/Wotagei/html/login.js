function validateForm() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    // Read the text file containing the credentials
    fetch('credentials.txt')
        .then(response => response.text())
        .then(data => {
            // Split the text file data into lines
            var lines = data.split('\n');

            // Loop through the lines and check for a match
            var match = false;
            for (var i = 0; i < lines.length; i++) {
                var line = lines[i].trim();
                var credentials = line.split(',');

                // Check if the username and password match
                if (credentials[0] === username && credentials[1] === password) {
                    match = true;
                    var role = credentials[2].trim();
                    if (role === 'fan') {
                        alert('Welcome ' + username + ' (Fan)');
                        window.location.href = 'fan.html'; // Redirect to fan page
                    } else if (role === 'idol') {
                        alert('Welcome ' + username + ' (Idol)');
                        window.location.href = 'idol.html'; // Redirect to idol page
                    }
                    break;
                }
            }

            // If no match is found, display error message
            if (!match) {
                alert('Invalid username or password');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred while logging in');
        });

    return false; // Prevent form submission
}
