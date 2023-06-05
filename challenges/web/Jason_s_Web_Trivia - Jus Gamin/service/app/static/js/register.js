const show_message = (msg) => {
  $('.error').css('display', 'block')

  if (msg) {
    $('.error').html(msg)
  }

  setTimeout(() => {
      $('.error').css('display', 'none')
  }, 10000)
}

const register = () => {
  let username = $('#username').val();
  let password = $('#password').val();
  let confirm_password = $('#confirm_password').val();

  if (!username || !password || !confirm_password) {
    show_message('Please fill in all fields');
    return;
  }

  if (password !== confirm_password) {
    show_message('Passwords do not match');
    return;
  }

  fetch('/api/register', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        'username': username,
        'password': password
    })
  })
  .then(res => {
    if (res.status === 200) {
      window.location.replace('/login');
    } else {
      res.json().then(data => {
        show_message(data['error']);
      })
    }
  }).catch((err) => {
    if (err) {
      console.log(err);
    }
  })
}