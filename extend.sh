su -c "cp /data/user/0/nextapp.fx/shared_prefs/nextapp.fx_preferences.xml . && chmod 666 nextapp.fx_preferences.xml" && \
python extend.py && \
su -c "cp nextapp.fx_preferences.xml /data/user/0/nextapp.fx/shared_prefs"
