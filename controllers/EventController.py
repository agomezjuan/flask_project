

def index():
    events = Event.query.all()
    return render_template('event/index.html', events=events)
