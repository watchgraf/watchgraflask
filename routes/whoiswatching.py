# -*- encoding: utf-8 -*-
from includes import *

@app.route('/who-is-watching', methods=['POST', 'GET'])
@app.route('/kim-izliyor', methods=['POST', 'GET'])
def whoiswatching():
    if not check_account(): return redirect(url_for('home'))
    profiles = profile.query.filter_by(idAccount = get_logged_account().idAccount).all()
    if len(profiles) > 0:
        # select function
        if request.args.get('select'):
            select_profile = profile.query.filter_by(idProfile=request.args.get('select')).first()
            if select_profile == None: return redirect(url_for('whoiswatching'))
            else:
                if select_profile.password == '': # '' stands for Empty passwords
                    session['login_type'] = 'PROFILE'
                    login_user(select_profile)
                    return redirect(url_for('home'))
                else: return redirect(url_for('whoiswatching_password') + '?profile=' + select_profile.idProfile)
        return render_template('whoiswatching/index.html', title='Kim İzliyor?', header=False, footer=False, profiles=profiles)
    else: return redirect(url_for('accountprofile_new'))

@app.route('/who-is-watching/password/' + str(id_generator(size=256)), methods=['POST', 'GET'])
@app.route('/kim-izliyor/parola/' + str(id_generator(size=256)), methods=['POST', 'GET'])
def whoiswatching_password():
    if check_account() == False: return redirect(url_for('home'))

    form = WhoIsWatchingPasswordForm()
    if form.validate_on_submit():
        select_profile = profile.query.filter_by(idProfile=request.args.get('profile')).first()
        if select_profile.password == form.password.data:
            session['login_type'] = 'PROFILE'
            login_user(select_profile)
            return redirect(url_for('home'))
        else: return error(err_msg='Yanlış bir şifre girdiniz.', ret_url=url_for('whoiswatching_password') + '?profile=' + request.args.get('profile'))

    if request.args.get('profile'):
        select_profile = profile.query.filter_by(idProfile=request.args.get('profile')).first()
        if select_profile == None: return redirect(url_for('home'))
        else:
            if select_profile.password == '': return redirect(url_for('whoiswatching'))
            else:
                return render_template('whoiswatching/password.html', title='Parola ile Giriş Yap', header=False, footer=False, select_profile=select_profile, form=form)
