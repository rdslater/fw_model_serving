# fw_model_serving
How to get flywheel to talk to outside containers
Phase 1:
Put a gear on flywheel, spin up a gear on a remote server and get them to talk

Notes:  
- When using WSL you need the WINDOWS docker and WSL extension! DOH!
- Agentic AI still bad at flywheel manifests.  Mininmal is attached.  Flywheel template is more than bare bones
- Running locally passed
- Running on linux reminder that 127.0.0.1 is inside the container! (warning in file with correction)

  ```
  flyw gear build .
  flyw gear config --input "input_file"="dummy.txt"
  flyw gear run --prepare
  flyw gear run /tmp/gear/<yourgearnamehere>
  ```
  setup ngrok to tunnel with success to wisc.flywheel.io version 0.0.2 (had to change port to 8008 as others were using port 8000)

  Completed 5/26/26
  Phase 2:
  

  
