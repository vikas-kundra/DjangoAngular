var xhr = new XMLHttpRequest();
document.getElementById("myform").onsubmit = function(e) {


    var t="";
	var f = e.target,
		formData = new FormData(f);

     xhr.onreadystatechange = function() {
     console.log(xhr.readyState, xhr.responseText);
        if (xhr.readyState < 4)                         // while waiting response from server
            document.getElementById('demo').innerHTML = "Loading...";
         else if (xhr.readyState === 4) {                // 4 = Response from server has been completely loaded.
            if (xhr.status == 200 && xhr.status < 300)  // http status between 200 to 299 are all successful
                document.getElementById('demo').value = xhr.responseText;
           }
}

    xhr.setRequestHeader('X-CSRF-Token', getCSRFTokenValue());
	xhr.open("POST", f.action);

    xhr.send(formData);

}

function ajax_response() {
  if(xhr.readyState == 4 && xhr.status == 200) {
    document.getElementById("demo").innerHTML = xhr.responseText;

  }
}

function abc(){
   var t="";
	var f = e.target,
		formData = new FormData(f);

     xhr.onreadystatechange = function() {
     console.log(xhr.readyState, xhr.responseText);
        if (xhr.readyState < 4)                         // while waiting response from server
            document.getElementById('demo').innerHTML = "Loading...";
         else if (xhr.readyState === 4) {                // 4 = Response from server has been completely loaded.
            if (xhr.status == 200 && xhr.status < 300)  // http status between 200 to 299 are all successful
                document.getElementById('demo').value = xhr.responseText;
           }
}

    xhr.setRequestHeader('X-CSRF-Token', getCSRFTokenValue());
	xhr.open("POST", f.action);

    xhr.send(formData);



}