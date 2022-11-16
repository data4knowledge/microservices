osascript -e 'tell app "Terminal" to do script "cd ~/Documents/python/ra_service &&
ls &&
source .venv/bin/activate &&
uvicorn main:app --reload --port 8010"'

osascript -e 'tell app "Terminal" to do script "cd ~/Documents/python/crm_service &&
ls &&
source .venv/bin/activate &&
uvicorn main:app --reload --port 8011"'

osascript -e 'tell app "Terminal" to do script "cd ~/Documents/python/ct_service &&
ls &&
source .venv/bin/activate &&
uvicorn main:app --reload --port 8012"'

osascript -e 'tell app "Terminal" to do script "cd ~/Documents/python/bc_service &&
ls &&
source .venv/bin/activate &&
uvicorn main:app --reload --port 8013"'

osascript -e 'tell app "Terminal" to do script "cd ~/Documents/python/study_service &&
ls &&
source .venv/bin/activate &&
uvicorn main:app --reload --port 8014"'

osascript -e 'tell app "Terminal" to do script "cd ~/Documents/python/study_import_service &&
ls &&
source .venv/bin/activate &&
uvicorn main:app --reload --port 8015"'

osascript -e 'tell app "Terminal" to do script "cd ~/Documents/python/form_service &&
ls &&
source .venv/bin/activate &&
uvicorn main:app --reload --port 8016"'

osascript -e 'tell app "Terminal" to do script "cd ~/Documents/python/sdtm_service &&
ls &&
source .venv/bin/activate &&
uvicorn main:app --reload --port 8017"'

osascript -e 'tell app "Terminal" to do script "cd ~/Documents/python/study_data_import_service &&
ls &&
source .venv/bin/activate &&
uvicorn main:app --reload --port 8018"'

osascript -e 'tell app "Terminal" to do script "cd ~/Documents/python/ct_ui &&
ls &&
source .venv/bin/activate &&
uvicorn main:app --reload --port 8000"'

osascript -e 'tell app "Terminal" to do script "cd ~/Documents/python/bc_ui &&
ls &&
source .venv/bin/activate &&
uvicorn main:app --reload --port 8001"'

osascript -e 'tell app "Terminal" to do script "cd ~/Documents/python/study_ui &&
ls &&
source .venv/bin/activate &&
uvicorn main:app --reload --port 8002"'

osascript -e 'tell app "Terminal" to do script "cd ~/Documents/python/form_ui &&
ls &&
source .venv/bin/activate &&
uvicorn main:app --reload --port 8003"'

osascript -e 'tell app "Terminal" to do script "cd ~/Documents/python/sdtm_ui &&
ls &&
source .venv/bin/activate &&
uvicorn main:app --reload --port 8004"'
