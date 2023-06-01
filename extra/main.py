from flask import Flask, render_template, request

import db

app = Flask(__name__, template_folder="template")


@app.route('/', methods=['POST', 'GET'])
def main():
    if request.method == 'POST':
        song = request.form['song']
        print(song)
        song = song.lower()
        song = song.rstrip()
        try:
            data = list(db.get_data(song))
            if data[0][3] is None:
                curr_info = list(data[0])
                curr_info[3] = 'The song from "' + data[0][1] + '" album.'
                data[0] = tuple(curr_info)

            path_song = "../songs/" + ((data[0][0].replace(" ", "_")).replace("?", "")).replace("'", "") + ".mp3"
            print(path_song)
            path_cover = "/static/pics/" + data[0][1].replace(" ", "") + ".png"
            print(path_cover)
            return render_template("info.html", data=data, path_song=path_song, path_cover=path_cover)
        except IndexError:
            return render_template("main.html")
    else:
        return render_template("main.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5500)
