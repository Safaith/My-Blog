from django.shortcuts import render
from datetime import date

# Create your views here.
all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "fahim",
        "date": date(2021, 7, 21),
        "title": "Mountain Hiking",
        "excerpt": """There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for that beautiful view!""",
        "content": """
          The hiking tours in the "mountain hiking" category lead you along hiking paths where sure-footedness and sometimes a head for heights are required. Particularly on the steeper, sometimes unpaved sections, surefootedness is an advantage. The daily stages are scheduled to take between four and about six and a half hours. On some mountain hiking tours, you can also expect smaller ascents to the summit. On a mountain hike, you will cover longer distances and climb a few metres in altitude. This is our difficulty level three, but on the day tours you will be rewarded with unforgettable-beautiful views and hiking experiences that you will remember for a long time.
        """
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "tanjim",
        "date": date(2022, 3, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
        First is the sheer joy of making things. As the child delights in his mud pie, so the adult enjoys building things, especially things of his own design. I think this delight must be an image of God's delight in making things, a delight shown in the distinctiveness of each leaf and each snowflake.
        Second is the pleasure of making things that are useful to other people.Deep within, we want others to use our work and to find it helpful. In this respect the programming system is not essentially different from the child's first clay pencil holder "for Daddy's office.
        """
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "safaith",
        "date": date(2020, 8, 5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
                Wood has the best thermal insulation properties of any mainstream construction material. When sourced from sustainably managed forests it can actually be better than carbon neutral.
                As a natural product and every piece, regardless of species, is completely unique. This means that it can vary dramatically in appearance (even form the same tree/board). This adds to the character, diversity and beauty of the material – but is also something to consider if you are expecting all pieces to look alike.
                Wood is a hard, fibrous structural tissue found in the stems and roots of trees and other woody plants. It has been used for thousands of years for both fuel and as a construction material. It is an organic material, a natural composite of cellulose fibres (which are strong in tension) embedded in a matrix of lignin which resists compression.
                    """
    }
]
def get_date(post):
    return post['date']

def index(request):
    sorted_post = sorted(all_posts,key=get_date)
    latest_posts = sorted_post[-3:] 
    return render(request, "blog/index.html",{
        "posts": latest_posts
    })


def posts(request):
    return render(request,"blog/all-posts.html",{
        "all_posts":all_posts
    })


def post_details(request,slug):
    identify_post = next(post for post in all_posts if post['slug']==slug )
    return render(request,"blog/post-detail.html",{
        "post":identify_post
    })
