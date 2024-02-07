function ajaxGetRequest(path, callback){
  let request = new XMLHttpRequest();
  request.onreadystatechange = function(){
    if (this.readyState === 4 && this.status === 200){
        callback(this.response);
    }
  };
  request.open("GET", path);
  request.send();
}

function ajaxPostRequest(path, data, callback){
  let request = new XMLHttpRequest();
  request.onreadystatechange = function(){
    if (this.readyState === 4 && this.status === 200){
      callback(this.response);
    }
  };
  request.open("POST", path);
  request.send(data);
}


document.getElementById('myForm').addEventListener('submit', function(e) {
    e.preventDefault();

    let dropdown1 = document.querySelector('select[name="dropdown1"]').value;
    let dropdown2 = document.querySelector('select[name="dropdown2"]').value;
    let dropdown3 = document.querySelector('select[name="dropdown3"]').value;
    let textfield = document.querySelector('input[name="textfield"]').value;
    let textfield2 = document.querySelector('input[name="textfield2"]').value;
    let textfield_key = document.querySelector('input[name="textfield_key"]').value;
    let textfield3 = document.querySelector('input[name="textfield3"]').value;

    let data = new FormData();
    data.append('dropdown1', dropdown1);
    data.append('dropdown2', dropdown2);
    data.append('dropdown3', dropdown3);
    data.append('textfield', textfield);
    data.append('textfield_key', textfield_key);
    data.append('textfield2', textfield2);
    data.append('textfield3', textfield3);

    ajaxPostRequest('/submit', data, function(response) {
        document.getElementById('result').innerHTML = response;
    });
});
