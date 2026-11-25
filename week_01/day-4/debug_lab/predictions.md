# prediction for save_day.sh

### file `git diff --cached --name-only` shows:
files staged:
`.gitignore`
`.env`
`week-01/day-3/weather-card/.venv/pyvenv.cfg`
`week-01/day-4/debug_lab/save_day.sh`
`week-01/day-4/notes.md`
`week-01/day-4/debug_lab/predictions.md`

I predict the commit message will cause an error
beacuse the script passes the commit message variable (`$msg`) without double quotes `git commit -q -m $msg`
