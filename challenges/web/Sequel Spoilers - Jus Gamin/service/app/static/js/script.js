const show_message = (msg) => {
  $('.error').css('display', 'block')

  if (msg) {
    $('.error').html(msg)
  }

  setTimeout(() => {
    $('.error').css('display', 'none')
  }, 10000)
}

const login = () => {
  let username = $('#username').val();
  let password = $('#password').val();

  if ($.trim(username) === '' || $.trim(password) === '') {
    show_message('Please fill in all fields');
    return;
  }

  fetch('/api/login', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      'username': username,
      'password': password
    })
  })
  .then((res) => {
    if (res.status === 200){
      window.location.replace('/home');
    } else {
      res.json()
      .then((data) => {
        show_message(data['error']);
      });
    }
  });
}