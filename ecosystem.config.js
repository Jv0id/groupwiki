module.exports = {
  apps : [{
    name: 'groupwiki',
    script: 'python3 bot.py',
    instances: 1,
    autorestart: true,
  }]
};
