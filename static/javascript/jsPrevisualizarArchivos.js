document.addEventListener('DOMContentLoaded', function() {
    const imagenesInput = document.getElementById('imagenes');
    const videosInput = document.getElementById('videos');
    const imagenesPreviewsDiv = document.getElementById('imagenes-previews');
    const videosPreviewsDiv = document.getElementById('videos-previews');

    function handleFileSelect(input, type) {
        const previewsDiv = type === 'image' ? imagenesPreviewsDiv : videosPreviewsDiv;
        previewsDiv.innerHTML = ''; 
        const files = input.files;

        for (const file of files) {
            const reader = new FileReader();

            reader.onload = function(e) {
                const result = e.target.result;
                let element;

                if (type === 'image') {
                    element = document.createElement('img');
                    element.src = result;
                    element.alt = 'Vista previa de la imagen';
                    element.style.maxWidth = '100px'; 
                    element.style.marginRight = '10px'; 
                } else if (type === 'video') {
                    element = document.createElement('video');
                    element.src = result;
                    element.controls = true;
                    element.style.maxWidth = '200px'; 
                    element.style.marginRight = '10px'; 
                }

                previewsDiv.appendChild(element);
            };

            reader.readAsDataURL(file);
        }
    }

    imagenesInput.addEventListener('change', function() {
        handleFileSelect(this, 'image');
    });

    videosInput.addEventListener('change', function() {
        handleFileSelect(this, 'video');
    });
});