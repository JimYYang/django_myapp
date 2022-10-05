#! /bin/zsh
#第一行到底怎么写是存在细节问题

JS_PATH=/home/dj_acs/myapp/game/static/js/
JS_PATH_DIST=${JS_PATH}dist/
JS_PATH_SRC=${JS_PATH}src/


find $JS_PATH_SRC -type f -name '*.js' | sort | xargs cat > ${JS_PATH_DIST}game.js
