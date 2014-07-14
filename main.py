import os
import buzzy
import subprocess

from scss import Scss
from datetime import datetime


class StaticSite(buzzy.Base):

    INCLUDE = ['static', 'favicon.ico', 'robots.txt', 'data.json']
    TEMPLATES_DIR = buzzy.Base.BASE_DIR

    @buzzy.register
    def index(self):
        yield buzzy.render.template('index.html', "index.html")

    @buzzy.register
    def blog(self):
        BLOG_DIR = os.path.join(self.BASE_DIR, "blog")
        BLOG_DATE_FORMAT = "%d-%m-%Y"

        posts = []
        for post in os.listdir(BLOG_DIR):
            post_path = os.path.join(BLOG_DIR, post)
            if post_path.endswith('md'):
                posts.append(
                    buzzy.render.markdown(post_path, post.replace('.md','.html'))
                )

        posts.sort(
            key=lambda x: datetime.strptime(x.meta['date'], BLOG_DATE_FORMAT),
            reverse=True
        )

        yield buzzy.render.template('blog.html', "blog", posts=posts)

    @buzzy.register
    def css(self):
        content = Scss().compile(open(self.BASE_DIR / 'static/main.scss').read())
        yield buzzy.render.content('static/main.css', content)

    @buzzy.command
    def deploy(self, args):
        self.build(args)

        git_thing = [
            "git init",
            "git remote add origin git@github.com:hippyvm/hippyvm.github.io.git",
            "git add .",
            "git commit -m 'page generated'",
            "git push --force -u origin master "
        ]

        for each in git_thing:
            print subprocess.check_output(each, shell=True, cwd=self.BUILD_DIR)

        self.logger.info("Deployed")



if __name__ == "__main__":
    StaticSite()
