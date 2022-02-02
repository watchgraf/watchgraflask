# -*- encoding: utf-8 -*-
from includes import *

"""
// ninja functions
"""

# THIS IS FUCKED UP,
# I DON'T KNOW WHAT TO DO
# WITH ALL THAT MESS

@app.context_processor
def utility_processor():
    def get_content_db(content_id): return content.query.filter_by(idContent=content_id).first()
    def get_profile_db(profile_id): return profile.query.filter_by(idProfile=profile_id).first()
    def get_account_db(account_id): return account.query.filter_by(idAccount=account_id).first()
    def get_cast_db(cast_id): return cast.query.filter_by(idCast=cast_id).first()
    def get_highlightcontent_db_by_contentid(content_id): return highlightContent.query.filter_by(idContent=content_id).first()
    def get_path(get_variable=None):
        return_path = os.path.join(os.path.dirname(app.instance_path))
        if get_variable: os.path.join(return_path, get_variable)
        else: pass
        return return_path
    def get_tvseasoncontent_db_by_idcontent(content_id):
        return tvSeasonContent.query.filter_by(idContent=content_id).order_by(tvSeasonContent.seasonNumber.asc()).order_by(tvSeasonContent.seasonNumber.asc()).all()
    def get_tvepisodecontent_db_by_idcontent_and_seasonnumber(content_id, season_number):
        return tvEpisodeContent.query.filter(and_(tvEpisodeContent.idContent == content_id, tvEpisodeContent.seasonNumber == season_number)).order_by(tvEpisodeContent.episodeNumber.asc()).all()
    def get_firsttvepisodeplayer_by_idcontent_seasonnumber_episodenumber(content_id, season_number, episode_number):
        first_player = tvPlayer.query.filter(and_(tvPlayer.idContent == content_id, tvPlayer.seasonNumber == season_number, tvPlayer.episodeNumber == episode_number)).first()
        if first_player != None: return first_player.idPlayer
        else: return 'not any player'
    ## tv
    def get_tv_seasonlist(content_id):
        select_content = content.query.filter(and_(content.idContent == str(content_id), content.type == 'TV')).first()
        if select_content == None: return 1

        select_all_seasons = tvSeasonContent.query.filter(and_(tvSeasonContent.idContent == str(content_id))).order_by(tvSeasonContent.seasonNumber.asc()).all()
        if select_all_seasons == None: return 1

        return select_all_seasons
    def get_tv_episodelist(content_id, season_id):
        select_content = content.query.filter(and_(content.idContent == str(content_id), content.type == 'TV')).first()
        if select_content == None: return 1

        select_all_episodes = tvEpisodeContent.query.filter(and_(tvEpisodeContent.idContent == str(content_id), tvEpisodeContent.idTvSeason == str(season_id))).order_by(tvEpisodeContent.episodeNumber.asc()).all()
        if select_all_episodes == None: return 1

        return select_all_episodes
    ## end tv
    ## card details
    def get_moviecontent_latestplayer(content_id):
        select_content = content.query.filter(and_(content.idContent == str(content_id), content.type == 'MOVIE')).first()
        if select_content == None: return 1

        select_latest_player = moviePlayer.query.filter(and_(moviePlayer.idContent == str(select_content.idContent), moviePlayer.visibility == True)).order_by(moviePlayer.addDate.desc()).first()
        if select_latest_player == None: return 1

        return select_latest_player
    def get_tvcontent_latestepisode(content_id):
        select_content = content.query.filter(and_(content.idContent == str(content_id), content.type == 'TV')).first()
        if select_content == None: return 1

        select_latest_episode = tvEpisodeContent.query.filter(and_(tvEpisodeContent.idContent == str(select_content.idContent), tvEpisodeContent.visibility == True)).order_by(tvEpisodeContent.addDate.desc()).first()
        if select_latest_episode == None: return 1

        return select_latest_episode
    ## end card details
    ## tvtitlecomment
    def get_tvtitlecomment(comment_id):
        return tvTitleComment.query.filter_by(idComment=comment_id).first()
    def get_tvtitlecomment_replies(comment_id):
        return tvTitleComment.query.filter_by(replyTo=comment_id).order_by(tvTitleComment.addDate.asc()).all()
    def get_tvtitlecomment_rates(content_id, tv_season_id, comment_id, rate_type):
        if rate_type == 'LIKE' or rate_type == 'DISLIKE':
            return tvTitleCommentRate.query.filter(and_(tvTitleCommentRate.idContent == content_id, tvTitleCommentRate.idTvSeason == tv_season_id, tvTitleCommentRate.idComment == comment_id, tvTitleCommentRate.rateType == rate_type)).all()
    def get_tvtitlecomment_rate(comment_id, profile_id, rate_type):
        if rate_type == 'LIKE' or rate_type == 'DISLIKE':
            return tvTitleCommentRate.query.filter(and_(tvTitleCommentRate.idComment == comment_id, tvTitleCommentRate.idRateProfile == profile_id, tvTitleCommentRate.rateType == rate_type)).first()
    ## end tvtitlecomment
    ## tvcomment
    def get_tvcomment(comment_id):
        return tvComment.query.filter_by(idComment=comment_id).first()
    def get_tvcomment_replies(comment_id):
        return tvComment.query.filter_by(replyTo=comment_id).order_by(tvComment.addDate.asc()).all()
    def get_tvcomment_rates(content_id, tv_season_id, tv_episode_id, comment_id, rate_type):
        if rate_type == 'LIKE' or rate_type == 'DISLIKE':
            return tvCommentRate.query.filter(and_(tvCommentRate.idContent == content_id, tvCommentRate.idTvSeason == tv_season_id, tvCommentRate.idTvEpisode == tv_episode_id, tvCommentRate.idComment == comment_id, tvCommentRate.rateType == rate_type)).all()
    def get_tvcomment_rate(comment_id, profile_id, rate_type):
        if rate_type == 'LIKE' or rate_type == 'DISLIKE':
            return tvCommentRate.query.filter(and_(tvCommentRate.idComment == comment_id, tvCommentRate.idRateProfile == profile_id, tvCommentRate.rateType == rate_type)).first()
    ## end tvcomment
    ## moviecomment
    def get_moviecomment(comment_id):
        return movieComment.query.filter_by(idComment=comment_id).first()
    def get_moviecomment_replies(comment_id):
        return movieComment.query.filter_by(replyTo=comment_id).order_by(movieComment.addDate.asc()).all()
    def get_moviecomment_rates(content_id, comment_id, rate_type):
        if rate_type == 'LIKE' or rate_type == 'DISLIKE':
            return movieCommentRate.query.filter(and_(movieCommentRate.idContent == content_id, movieCommentRate.idComment == comment_id, movieCommentRate.rateType == rate_type)).all()
    def get_moviecomment_rate(comment_id, profile_id, rate_type):
        if rate_type == 'LIKE' or rate_type == 'DISLIKE':
            return movieCommentRate.query.filter(and_(movieCommentRate.idComment == comment_id, movieCommentRate.idRateProfile == profile_id, movieCommentRate.rateType == rate_type)).first()
    ## end moviecomment
    ## castcomment
    def get_castcomment(comment_id):
        return castComment.query.filter_by(idComment=comment_id).first()
    def get_castcomment_replies(comment_id):
        return castComment.query.filter_by(replyTo=comment_id).order_by(castComment.addDate.asc()).all()
    def get_castcomment_rates(cast_id, comment_id, rate_type):
        if rate_type == 'LIKE' or rate_type == 'DISLIKE':
            return castCommentRate.query.filter(and_(castCommentRate.idCast == cast_id, castCommentRate.idComment == comment_id, castCommentRate.rateType == rate_type)).all()
    def get_castcomment_rate(comment_id, profile_id, rate_type):
        if rate_type == 'LIKE' or rate_type == 'DISLIKE':
            return castCommentRate.query.filter(and_(castCommentRate.idComment == comment_id, castCommentRate.idRateProfile == profile_id, castCommentRate.rateType == rate_type)).first()
    ## end castcomment
    ## content genre
    def get_content_genre(content_id):
        select_content = content.query.filter_by(idContent=content_id).first()
        if select_content == None: return 1
        if select_content.type == 'MOVIE': return movieContentGenre.query.filter_by(idContent=content_id).all()
        elif select_content.type == 'TV': return tvContentGenre.query.filter_by(idContent=content_id).all()
        else: return 1
    def get_genre_list(genre_id, content_type):
        if content_type == 'MOVIE': return movieGenreList.query.filter_by(idGenre=genre_id).first()
        elif content_type == 'TV': return tvGenreList.query.filter_by(idGenre=genre_id).first()
        else: return 1
    ## end content genre
    ## content language
    def get_content_language(content_id):
        select_content = content.query.filter_by(idContent=content_id).first()
        if select_content == None: return 1
        return contentLanguage.query.filter_by(idContent=content_id).all()
    def get_language_list(language_idiso_639_1):
        return languageList.query.filter_by(idISO_639_1=language_idiso_639_1).first()
    ## end content language
    ## content country
    def get_content_country(content_id):
        select_content = content.query.filter_by(idContent=content_id).first()
        if select_content == None: return 1
        return contentCountry.query.filter_by(idContent=content_id).all()
    def get_country_list(country_idiso_3166_1):
        return countryList.query.filter_by(idISO_3166_1=country_idiso_3166_1).first()
    ## end content country
    return dict(sql_execute=sql_execute, \
                check_account=check_account, \
                check_profile=check_profile, \
                check_admin=check_admin, \
                get_content_db=get_content_db, \
                get_profile_db=get_profile_db, get_account_db=get_account_db, \
                get_cast_db=get_cast_db, \
                get_highlightcontent_db_by_contentid=get_highlightcontent_db_by_contentid, \
                get_path=get_path, \
                get_tvepisodecontent_db_by_idcontent_and_seasonnumber=get_tvepisodecontent_db_by_idcontent_and_seasonnumber, \
                get_tvseasoncontent_db_by_idcontent=get_tvseasoncontent_db_by_idcontent, \
                get_firsttvepisodeplayer_by_idcontent_seasonnumber_episodenumber=get_firsttvepisodeplayer_by_idcontent_seasonnumber_episodenumber, \
                get_tvcomment=get_tvcomment, get_tvcomment_replies=get_tvcomment_replies, get_tvcomment_rates=get_tvcomment_rates, get_tvcomment_rate=get_tvcomment_rate, \
                get_tv_seasonlist=get_tv_seasonlist, get_tv_episodelist=get_tv_episodelist, \
                get_moviecontent_latestplayer=get_moviecontent_latestplayer, get_tvcontent_latestepisode=get_tvcontent_latestepisode, \
                get_tvtitlecomment=get_tvtitlecomment, get_tvtitlecomment_replies=get_tvtitlecomment_replies, get_tvtitlecomment_rates=get_tvtitlecomment_rates, get_tvtitlecomment_rate=get_tvtitlecomment_rate, \
                get_moviecomment=get_moviecomment, get_moviecomment_replies=get_moviecomment_replies, get_moviecomment_rates=get_moviecomment_rates, get_moviecomment_rate=get_moviecomment_rate, \
                get_castcomment=get_castcomment, get_castcomment_replies=get_castcomment_replies, get_castcomment_rates=get_castcomment_rates, get_castcomment_rate=get_castcomment_rate, \
                get_content_genre=get_content_genre, get_genre_list=get_genre_list, \
                get_content_language=get_content_language, get_language_list=get_language_list, \
                get_content_country=get_content_country, get_country_list=get_country_list, \
                get_logged_account=get_logged_account, get_logged_profile=get_logged_profile, \
                format_date=format_date, format_datetime=format_datetime, format_time=format_time)
