# Steps to create migration: 

1. `cd` to the **db** directory 
   * `` cd backend/db``
   
2. run:
   * ``export PYTHONPATH="/home/gpt15/Desktop/statScribeServer:$PYTHONPATH"``
   
3. `cd` to the **docker** directory 
   * `` cd backend/docker``
   
4. run: 
   * ``docker compose up``

5. `cd` to the `backend/db` directory 
   * `` cd backend/db``

6. ????? edit your migration script? but not sure what that is atm. 

7. run 
   * ``alembic revision --autogenerate -m "version message"``