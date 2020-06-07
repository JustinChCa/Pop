$(document).ready(function () {
  var socket;
  socket = io.connect('http://' + document.domain + ':' + location.port);

  socket.on('message', function (json) {
    $('#msgBoard').append("<li class='list-group-item'>" + json.msg + "</li>");
    document.documentElement.scrollTop = document.documentElement.scrollHeight;
  });
  $('#msgForm').on('submit', function (e) {
    e.preventDefault();
    socket.emit('message', { 'msg': $('#message').val() });
  });
});