const show_message = (msg) => {
  $('.error').css('display', 'block')

  if (msg) {
    $('.error').html(msg)
  }

  setTimeout(() => {
      $('.error').css('display', 'none')
  }, 10000)
}

const create = () => {
  let question = $('#question').val();
  let answer = $('#answer').val();

  if (!question || !answer) {
    show_message('Please fill in all fields');
    return;
  }

  fetch('/api/create', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        'question': question,
        'answer': answer
    })
  })
  .then(res => {
    if (res.status === 200) {
      window.location.replace("/profile");
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