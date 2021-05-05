from manim import *
class SquareToCircle(Scene):
    def construct(self):
        names = Text("Justin, Sam, Zain, and Laksh")

        title = Text("Collatz Conjecture")
        title.scale(1.5)

        # Initial introduction
        self.play(Write(names),run_time=4)
        self.play(names.animate.scale(0.75).to_corner(DR))
        self.play(Write(title))

        # Maybe add something here
        self.wait()

        # History of the conjecture
        self.play(title.animate.scale(0.75).to_corner(UL), FadeOut(names))
        collatz_image = ImageMobject("media/images/scene/lothar_collatz.jpg")
        collatz_image.scale(1.75)
        collatz_image.to_edge(LEFT)
        collatz_name = Text("Lothar Collatz")
        collatz_name.next_to(collatz_image, DOWN)

        collatz_proposition_year = Text("1931").move_to(LEFT * 2)
        this_year = Text("2021").to_edge(RIGHT * 2)
        double_arrow = DoubleArrow(start=collatz_proposition_year.get_right(), end=this_year.get_left())
        year_diff = Text("84 Years!", color=YELLOW).next_to(double_arrow, DOWN).scale(0.8)

        year_group = Group(collatz_proposition_year, this_year, double_arrow, year_diff)
        year_group.next_to(collatz_image, RIGHT * 2).shift(DOWN * 0.5)

        self.play(FadeIn(collatz_image), Write(collatz_name))
        self.play(Write(collatz_proposition_year))
        self.play(Write(this_year))
        self.play(FadeIn(double_arrow))
        self.play(Write(year_diff))
        self.play(year_group.animate.shift(UP))

        surprise = Text("No one has successfully proven it")
        surprise.next_to(year_group, DOWN * 4).scale(0.8)
        asterisk = Text("*", color=YELLOW).next_to(surprise, RIGHT)


        self.play(Write(surprise))
        self.play(Write(asterisk))

class History(Scene):
    def construct(self):
        title = Text("Collatz Conjecture")
        title.to_corner(UL)

        kakutani_image = ImageMobject("media/images/scene/Shizuo_Kakutani.jpg")
        kakutani_image.to_edge(LEFT).scale(1.75).shift(RIGHT).shift(DOWN * 0.15)

        kakutani_name = Text("Shizuo Kakutani")
        kakutani_name.scale(0.95).next_to(kakutani_image, DOWN)

        kakutani_group = Group(kakutani_image, kakutani_name)

        subs = self.get_substrings("\"For about a month everybody at Yale worked on it, with no result. A similar phenomenon happened when I mentioned it at the University of Chicago. A joke was made that this problem was part of a conspiracy to slow down mathematical research in the U.S.\"")
        kakutani_text = Paragraph(*subs)
        kakutani_text.scale(0.6).next_to(kakutani_group, RIGHT)

        self.add(title)
        self.add(kakutani_image)
        self.add(kakutani_name)
        self.add(kakutani_text)

    def get_substrings(self, input):
        list = []
        while len(input) > 50:
            list.append(input[:50])
            input = input[50:]
        else:
            list.append(input[:])
        return list


