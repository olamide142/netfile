
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


$(document).ready(function(){

    
    // function join_netfile(){
    //     alert(1);
    //     $.ajax({
    //         url: '/join',
    //         method: 'POST',
    //         data : {'username':this.username, 'csrfmiddlewaretoken':getCookie('csrftoken')},
    //         success: function (data) {
    //             console.log("Done");
    //         },
    //         error: function (error) {
    //         console.log(error);
    //         }
    //     });
    // } 


});
function fileData(){
    // Get file name and extension 
    var extension = document.getElementById('file').value;
    console.log(extension);
    var extension = extension.split('.');
    document.getElementById('file_extension').value = extension[extension.length-1];

    extension.pop();
    document.getElementById('file_name').value = extension.join(".");
    document.getElementById('file_label').textContent = extension.join(".").replace("C:\\fakepath\\",'');

    // Get file size 
    const fi = document.getElementById('file');
    var file = 0;
    if (fi.files.length > 0){
        for (var i = 0; i < fi.files.length; i++){
            var fsize = fi.files.item(i).size;
            console.log(fsize);
        }
    }
    
    document.getElementById('filesize').value = fsize;

    
}
