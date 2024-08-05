// backend/docker/mongo-init/init-mongo.js
db.createUser({
    user: "stat_scribe_user",
    pwd: "stat_scribe_password",
    roles: [
        {
            role: "readWrite",
            db: "stat_scribe"
        }
    ]
});