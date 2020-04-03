var EXTENSION;
var FILENAME;
var FSIZE;
var FILE;

$(document).ready(function(){
    $('#downloading').hide();
    $('#download_btn').click(function(){
        $('#downloading').show();
        setTimeout(function(){
            $('#downloading').hide();
        }, 5000);

    });


    $('#uploading').hide();
    $('#upload-file').click(function(){
        $('#uploading').show();
    });
});


function fileData(){
    // Get file name and extension 
    var extension = document.getElementById('file').value;
    console.log(extension);
    var extension = extension.split('.');
    EXTENSION = extension[extension.length-1];
    document.getElementById('file_extension').value = EXTENSION;


    extension.pop();
    document.getElementById('file_name').value = extension.join(".").replace("C:\\fakepath\\",'');
    document.getElementById('file_label').textContent = extension.join(".").replace("C:\\fakepath\\",'');
    FILENAME = extension.join(".").replace("C:\\fakepath\\",'');

    // Get file size 
    const fi = document.getElementById('file');
    if (fi.files.length > 0){
        for (var i = 0; i < fi.files.length; i++){
            var fsize = fi.files.item(i).size;
            FILE = fi.files;
            console.log(fsize);
        }
    }
    
    document.getElementById('file_size').value = fsize;
    FSIZE = fsize;

    
}

