## Whiskerboard python client

Example usage:
  
```python
import whiskerboardclient

status = whiskerboardclient.WhiskerBoard(host='status.example.com', port='80')
status.update_status('up', 'The service status message', 'servicename')
```
