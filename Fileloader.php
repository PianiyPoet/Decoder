<?php
if(isset($_FILES['file'])) {
    $file = $_FILES['file'];
    
    if($file['error'] === UPLOAD_ERR_OK) {
        $uploadDir = 'uploads/';
        $uploadFile = $uploadDir . basename($file['name']);
        
        if(move_uploaded_file($file['tmp_name'], $uploadFile)) {
            echo 'File uploaded successfully.';
        } else {
            echo 'Error uploading file.';
        }
    } else {
        echo 'Error: ' . $file['error'];
    }
} else {
    echo 'No file uploaded.';
}
?>