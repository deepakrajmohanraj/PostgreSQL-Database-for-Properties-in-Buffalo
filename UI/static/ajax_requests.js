function makeAjaxRequest(method, url, data, callback) {
  $.ajax({
    type: method,
    url: url,
    data: JSON.stringify(data),
    contentType: "application/json; charset=utf-8",
    dataType: "json",
    success: function(response) {
      console.log('success callback called');
      if (callback) {
        callback(response);
      }
    },
    error: function(xhr, textStatus, errorThrown) {
      console.log("error");
    }
  });
}

function makeAjaxCall(method, url) {
  $.ajax({
    type: method,
    url: url,
    contentType: "application/json; charset=utf-8",
    dataType: "json",
    success: function(response) {
      console.log('success callback called');
    },
    error: function(xhr, textStatus, errorThrown) {
      console.log("error");
    }
  });
}
// function makeAjaxRequest(method, url, data, callback) {
//   var xhr = new XMLHttpRequest();
//   xhr.open(method, url);
//   xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
//   xhr.onload = function() {
//     if (xhr.status === 200) {
//       console.log(xhr.responseText);
//       callback(xhr.response)
//     } else {
//       console.log("Request failed. Status: " + xhr.status);
//     }
//   };
//   xhr.onerror = function() {
//     console.log("Request failed. Network error.");
//   };
//   xhr.send(JSON.stringify(data));
// }
