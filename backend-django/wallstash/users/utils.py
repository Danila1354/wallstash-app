import os
import uuid

def user_avatar_upload_to(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{instance.username}-{uuid.uuid4().hex[:8]}.{ext}"
    return os.path.join("users", "avatars", filename)