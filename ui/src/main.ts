import './style.css';

import * as lib from './lib';

function lorem() {
  return [
    'Lorem ipsum dolor sit amet consectetur adipisicing elit. Beatae vitae nisi harum iusto debitis natus quibusdam? Deleniti, impedit id. Eos aut cum ipsa adipisci fugiat, ut amet voluptatum ad labore!',
    'Lorem ipsum dolor sit amet consectetur adipisicing elit. Beatae vitae nisi harum iusto debitis natus quibusdam? Deleniti, impedit id. Eos aut cum ipsa adipisci fugiat, ut amet voluptatum ad labore!',
    'Lorem ipsum dolor sit amet consectetur adipisicing elit. Beatae vitae nisi harum iusto debitis natus quibusdam? Deleniti, impedit id. Eos aut cum ipsa adipisci fugiat, ut amet voluptatum ad labore!',
    'Lorem ipsum dolor sit amet consectetur adipisicing elit. Beatae vitae nisi harum iusto debitis natus quibusdam? Deleniti, impedit id. Eos aut cum ipsa adipisci fugiat, ut amet voluptatum ad labore!',
    'Lorem ipsum dolor sit amet consectetur adipisicing elit. Beatae vitae nisi harum iusto debitis natus quibusdam? Deleniti, impedit id. Eos aut cum ipsa adipisci fugiat, ut amet voluptatum ad labore!',
    'Lorem ipsum dolor sit amet consectetur adipisicing elit. Beatae vitae nisi harum iusto debitis natus quibusdam? Deleniti, impedit id. Eos aut cum ipsa adipisci fugiat, ut amet voluptatum ad labore!',
    'Lorem ipsum dolor sit amet consectetur adipisicing elit. Beatae vitae nisi harum iusto debitis natus quibusdam? Deleniti, impedit id. Eos aut cum ipsa adipisci fugiat, ut amet voluptatum ad labore!',
    'Lorem ipsum dolor sit amet consectetur adipisicing elit. Beatae vitae nisi harum iusto debitis natus quibusdam? Deleniti, impedit id. Eos aut cum ipsa adipisci fugiat, ut amet voluptatum ad labore!'
  ].join(' ');
}

async function main() {
  console.log('main js')

  const $resultsPanel = document.getElementById("results-panel") as HTMLDivElement;
  const $fileUpload = document.getElementById("file_input") as HTMLInputElement;
  const $resultsText = document.getElementById("results-text") as HTMLPreElement;
  const $progressBar = document.getElementById("upload-progress") as HTMLDivElement;
  const $progressBarProgress = document.getElementById("upload-progress-bar") as HTMLDivElement;
  const $exportButtons = document.getElementById("export-buttons") as HTMLDivElement;
  const $exportAsTextButton = document.getElementById("export-text") as HTMLButtonElement;
  const $copyToClipboardButton = document.getElementById("copy-clipboard") as HTMLButtonElement;

  $fileUpload.addEventListener('change', (ev: Event) => {
    const uploadedFiles = $fileUpload.files;
    if (!uploadedFiles || !(uploadedFiles instanceof FileList)) return;

    const body = new FormData();
    body.append('file', uploadedFiles[0]);

    fetch('http://localhost:8000/transcribe', {
      method: 'POST',
      body,
    })
      .then(res => res.json())
      .then((data) => {
        console.log(data)
      })

  })

  function onInterval() {
    1
    console.log('interval js')
    console.log()
  }

  setTimeout(onInterval, 1000);
}

document.addEventListener('DOMContentLoaded', main);