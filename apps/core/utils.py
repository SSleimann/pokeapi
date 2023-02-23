def user_directory_path(instance, filename):
    return 'uploads/users/user_{0}/{1}'.format(instance.user.username, filename)

