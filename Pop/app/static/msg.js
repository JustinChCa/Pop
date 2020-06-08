$(document).ready(function () {
  var socket;
  var board = $('#msgBoard')
  var form = $('#msgForm')
  socket = io.connect('http://' + document.domain + ':' + location.port);

  socket.on('message', function (json) {
    board.append("<p class='text-left mb-1'>" + json.msg + "</p>");
    document.documentElement.scrollTop = document.documentElement.scrollHeight;
  });
  form.on('submit', function (e) {
    e.preventDefault();
    socket.emit('message', { 'msg': $('#message').val() });
    $('#message').val('');
  });
});

