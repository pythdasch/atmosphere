jQuery(document).ready(function() {
  var $ = jQuery;
 
  /*
  Execute revealDropzone() every 1000 milliseconds
    Identify all of the input fields - once all of them have been populated, 
      reveal the drop zone
    If any of the text inputs becomes empty again, hide the drop zone again
  */
  setInterval(revealDropzone, 1000);
  function revealDropzone(){
    var inputValues = $('#image_form input[type=text]').map(function() {
      return $(this).val();
    });
    for(var i=0;i<inputValues.length;i++){
      if(inputValues[i] === ""){
                // Hide the dropzone again if one of the fields becomes empty
        $("#dropzone").css("visibility", "hidden");
        return false;
      }
    }
    $("#dropzone").css("visibility", "visible");
    return true;
  }
 
  // The list of images we'll be creating via the drag and drop:
  var $list = $('#images_list');
  // Reference to the form
  var $form = $('#_form');
  
  // Utility functions:
 
  // For adding a dropped file to the list:
  function addItemToList(file) {
    var name = file.name;
 
    // "pending" - The image name will be greyed out until the upload returns success
    var $item = $('<li class="pending newitem" id="' + name + '">' + name + '</li>');
 
    // The remove button will be disabled until the upload returns success
    var $removeitem = $('<input id="remove_' + name + '" type="button" value="Remove" class="btn btn-mini btn-danger removebutton" disabled>');
    // ^^ btn, btn-mini, and btn-danger are Bootstrap classes
 
    $item.append($removeitem);
 
    // This click event is set so that the remove button executes removeItemFromList()
    $removeitem.click(removeItemFromList);
 
    $list.append($item);
    $item.data('removeElement', $removeitem);
 
    $item.data('name', name)
    $item.data('file', file);
    return $item;
  }
 
  // For removing a dropped file from the list:
  function removeItemFromList(event) {
    $(event.target).closest('li').remove();
    element = document.getElementById($(event.target)[0].id.replace("remove_", "image_"));
    element.parentNode.removeChild(element);
  }
 
  // For creating hidden form elements based on the response that's 
  // returned when the images are posted: 
  function addFormElements(response){
    // Split the response string ...
    var mySplitResult = response.split(";");
    for(i = 0; i < mySplitResult.length; i++){
      // And create an input for each image
      var input = document.createElement('INPUT');
      input.type = "hidden";
      // Input id and name are the image name prefixed with 'image_'
      input.id = "image_"+mySplitResult[i];
      input.name = "image_"+mySplitResult[i];
      input.value = mySplitResult[i];
      // Each new input is appended to the form named 'image_form'
      document.getElementById("image_form").appendChild(input);
    }
  }
 
  // This function is triggered when an event takes place in the dropzone area
  var dropHandler = function(e) {
  // Block default behavior on the drop zone element:
    e.preventDefault();
 
    // Capture files that have been dragged into the drop zone
    var files = e.originalEvent.dataTransfer.files;
 
    // Create the formData object that will be submitted via XMLHttpRequest
    var formData = new FormData();
    var fileElements = [];
    for (var i = 0; i < files.length; i++) {
      if($list[0].innerText.indexOf(files[i].name) === -1){
        // Append each file to the form, to an element named 'file':
        formData.append('file', files[i]);
        // Create for each file a form element to be displayed on the page:
        fileElements.push(addItemToList(files[i]));
      }
    }
    // Using Django 1.3 - a form post through XMLHttpRequest still requires this token
    var csrf_token = $('#csrfmiddlewaretoken').val()
    formData.append('csrfmiddlewaretoken', csrf_token)
 
    // Create an instance of XMLHttpRequest:
    var xhr = new XMLHttpRequest();
    // This posts back to the multi_image_upload_post() method we created in the admin.py (we haven't looked at that yet)
    var post_url = "/admin/images/image/image_upload/";
    xhr.open('POST', post_url);
    xhr.onload = function () {
      var i;
      var text = this.responseText;
      // If the image post was successful ...
      if (xhr.status === 200) {
        // ... add a hidden form element for each image so that the image names can be submitted with the main form post
        addFormElements(xhr.responseText);
        for (i = 0; i < fileElements.length; i++) {
          // The image is no longer pending upload, so remove that 'pending' class:
          fileElements[i].removeClass('pending');
          // Enable the "Remove" button for each image
          fileElements[i].data('removeElement').removeAttr('disabled');
        }
        // Images have been posted - the submit button can be enabled now
        $('#id_submit').removeAttr('disabled');
      } else {
        /*
          You should implement some better error handling than this, 
          but for now let's just apply a different class 
          to these elements so that the user knows something went wrong.
        */
        for (i = 0; i < fileElements.length; i++) {
          // Upload failed, the image name appears bold red
          fileElements[i].removeClass('pending').addClass('error');
          // Enable the "Remove" button for each image
          fileElements[i].data('removeElement').removeAttr('disabled');
        }
        // console.log('Something went wrong:' + xhr.status + xhr.responseText);
      }
    };
    // Here's where the form, with images attached, is actually posted:
    xhr.send(formData);
  }
 
  $('.dropzone').bind("dragenter", function(e) {
    e.preventDefault();
    $(e.target).addClass("hover");
  }).bind("dragleave", function(e) {
    e.preventDefault();
    $(e.target).removeClass("hover");
  }).bind("dragover", function(e) {
    e.preventDefault();
  }).bind("drop", dropHandler);
 
});