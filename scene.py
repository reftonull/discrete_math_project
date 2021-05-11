from manim import *
class Introduction(Scene):
    def construct(self):
        names = Text("Justin, Sam, Zain, and Laksh")

        title = Text("Collatz Conjecture")
        title.scale(1.5)

        # Initial introduction
        self.play(Write(names),run_time=4)
        self.play(names.animate.scale(0.75).to_corner(DR))
        self.play(Write(title))

        # Maybe add something here
        self.wait(12)

        # History of the conjecture
        self.play(title.animate.scale(0.75).to_corner(UL), FadeOut(names))
        collatz_image = ImageMobject("assets/lothar_collatz.jpg")
        collatz_image.scale(1.75)
        collatz_image.to_edge(LEFT)
        collatz_name = Text("Lothar Collatz")
        collatz_name.next_to(collatz_image, DOWN)

        collatz_proposition_year = Text("1937").move_to(LEFT * 2)
        this_year = Text("2021").to_edge(RIGHT * 2)
        double_arrow = DoubleArrow(start=collatz_proposition_year.get_right(), end=this_year.get_left())
        year_diff = Text("84 Years!", color=YELLOW).next_to(double_arrow, DOWN).scale(0.8)

        year_group = Group(collatz_proposition_year, this_year, double_arrow, year_diff)
        year_group.next_to(collatz_image, RIGHT * 2).shift(DOWN * 0.5)

        self.play(FadeIn(collatz_image), Write(collatz_name))
        self.play(Write(collatz_proposition_year))
        self.wait(4)
        self.play(Write(this_year))
        self.play(Create(double_arrow))
        self.play(Write(year_diff))
        self.wait(2)
        self.play(year_group.animate.shift(UP))

        surprise = Text("No one has successfully proven it")
        surprise.next_to(year_group, DOWN * 4).scale(0.8)
        asterisk = Text("*", color=YELLOW).next_to(surprise, RIGHT)


        self.play(Write(surprise), run_time=1.5)
        self.play(Write(asterisk))
        self.wait(13)

class History(Scene):
    def construct(self):
        title = Text("Collatz Conjecture")
        title.to_corner(UL)

        kakutani_image = ImageMobject("assets/Shizuo_Kakutani.jpg")
        kakutani_image.to_edge(LEFT).scale(1.75).shift(RIGHT).shift(DOWN * 0.15)

        kakutani_name = Text("Shizuo Kakutani")
        kakutani_name.scale(0.95).next_to(kakutani_image, DOWN)

        kakutani_group = Group(kakutani_image, kakutani_name)

        subs = self.get_substrings("\"For about a month everybody at Yale worked on it, with no result. A similar phenomenon happened     when I mentioned it at the University of Chicago. A joke was made that this problem was part of a  conspiracy to slow down mathematical research in  the U.S.\"", 50)
        kakutani_text = Paragraph(*subs)
        kakutani_text.scale(0.6).next_to(kakutani_group, RIGHT)

        self.add(title)
        self.play(FadeIn(kakutani_image), Write(kakutani_name))
        self.wait(5)
        self.play(Write(kakutani_text), run_time=19)
        self.play(FadeOut(kakutani_image), FadeOut(kakutani_name), FadeOut(kakutani_text))

        erdos_image = ImageMobject("assets/Erdos_budapest_fall_1992_(cropped).jpg")
        erdos_image.to_edge(LEFT).scale(1.75).shift(RIGHT)
        erdos_name = Text("Paul Erdős")
        erdos_name.scale(0.95).next_to(erdos_image, DOWN)

        erdos_group = Group(erdos_image, erdos_name)

        subs = self.get_substrings("\"Mathematics may not be ready for such   problems\"", 40)
        erdos_text = Paragraph(*subs)
        erdos_text.scale(0.75).next_to(erdos_group, RIGHT)

        self.wait(1)
        self.play(FadeIn(erdos_image), Write(erdos_name))
        self.wait(6)
        self.play(Write(erdos_text), run_time=5)
        self.play(FadeOut(erdos_group), FadeOut(erdos_text))

        leingang_image = ImageMobject("assets/Leingang_Matthew.jpg")
        leingang_image.to_edge(LEFT).scale(1.2).shift(RIGHT)
        leingang_name = Text("Matthew Leingang")
        leingang_name.scale(0.9).next_to(leingang_image, DOWN)

        leingang_group = Group(leingang_image, leingang_name)

        subs = self.get_substrings("\"How is something so simple to state so difficult to prove?\"", 40)
        leingang_text = Paragraph(*subs)
        leingang_text.scale(0.75).next_to(leingang_group, RIGHT)

        self.wait(1)
        self.play(FadeIn(leingang_image), Write(leingang_name))
        self.wait(6)
        self.play(Write(leingang_text), run_time=6)
        self.wait(3)
        self.play(FadeOut(leingang_group), FadeOut(leingang_text))

    def get_substrings(self, input, threshold):
        list = []
        while len(input) > threshold:
            list.append(input[:threshold])
            input = input[threshold:]
        else:
            list.append(input[:])
        return list

class Explanation(Scene):
    def construct(self):
        title = Text("Collatz Conjecture")
        title.to_corner(UL)

        self.add(title)

        complex_function = MathTex(r'\sum^n_{i=1} \log(i)^c \cdot i^d \cdot b^i \in \Theta(n^d \cdot log(n)^c \cdot b^n)').scale(1.3)
        think_about_it = Text("You be the judge!")
        think_about_it.shift(DOWN)

        self.play(Write(complex_function))
        self.wait(9)
        self.play(complex_function.animate.shift(UP))
        self.play(Write(think_about_it))
        self.wait(4)

        self.play(FadeOut(complex_function), FadeOut(think_about_it))

        collatz_left = MathTex(
            r"f(", r"n", r") = \begin{cases} \\ \\ \\ \end{cases}"
        ).shift(LEFT * 2)

        collatz_even_eq = MathTex(
            r"\frac{n}{2}"
        ).shift(UP * 0.5)

        collatz_odd_eq = MathTex(
            r"3n + 1"
        ).shift(DOWN * 0.5)

        collatz_even = MathTex(
            r"\text{if $n \equiv 0$ (mod 2)}"
        ).next_to(collatz_even_eq, RIGHT * 7)

        collatz_odd = MathTex(
            r"\text{if $n \equiv 1$ (mod 2)}"
        ).next_to(collatz_even, direction=DOWN * 2.2, aligned_edge=LEFT)

        collatz_right = Group(collatz_even_eq, collatz_odd_eq, collatz_odd, collatz_even)

        collatz_right.next_to(collatz_left, RIGHT)

        collatz_equation = Group(collatz_left, collatz_right)

        self.play(Write(collatz_left[0]), Write(collatz_left[2]))
        self.wait(5)
        self.play(Write(collatz_left[1]))
        self.wait(1)
        self.play(Write(collatz_even))
        self.wait(2)
        self.play(Write(collatz_even_eq))
        self.wait(2)
        self.play(Write(collatz_odd))
        self.wait(2)
        self.play(Write(collatz_odd_eq))

        self.play(collatz_equation.animate.shift(UP))

        collatz_example = MathTex("f(", "5", ") = ", "3n + 1 = ", "16")
        collatz_example.next_to(collatz_odd_eq, direction=DOWN * 6)

        self.wait(2)
        self.play(Write(collatz_example[0]), Write(collatz_example[2]))
        self.wait(1)
        self.play(Write(collatz_example[1]), Indicate(collatz_left[1]))
        self.wait(2)
        self.play(Write(collatz_example[3:]), Indicate(collatz_odd_eq), run_time=2)

        self.wait(5)
        self.play(FadeOut(collatz_example))
        self.wait(5)

        collatz_composition = MathTex(r"f \circ f", r"\circ f \circ \cdots \circ f", r"= 1")
        collatz_composition.next_to(collatz_odd_eq, direction=DOWN * 6)

        collatz_example.shift(DOWN)

        collatz_composition[0].shift(RIGHT * 1.8)

        self.play(Write(collatz_composition[0]))
        self.wait(19)
        self.play(Write(collatz_example))
        self.wait(3)

        collatz_example2 = MathTex(r"f(", r"16", r") = ", r"\frac{n}{2} = 8")
        collatz_example2.next_to(collatz_odd_eq, direction=DOWN * 9)

        self.play(ReplacementTransform(collatz_example, collatz_example2))
        self.wait(4)
        self.play(FadeOut(collatz_example2))

        self.play(collatz_composition[0].animate.shift(LEFT * 1.8))
        self.play(Write(collatz_composition[1]))

        collatz_composition_brace = Brace(collatz_composition[:2])
        brace_text = collatz_composition_brace.get_tex(r"\infty \text{ times}")

        self.play(Create(collatz_composition_brace), Write(brace_text))
        self.wait(5)
        self.play(Write(collatz_composition[2]))
        self.wait(7)
        self.play(FadeOut(collatz_composition), FadeOut(collatz_composition_brace), FadeOut(brace_text))

        collatz_general = MathTex(r"\forall x \in \mathbb{N}, \exists n \in \mathbb{N} : f^{(n)}(x) = 1")

        collatz_general.next_to(collatz_equation, direction=DOWN * 7).shift(LEFT)
        self.play(Write(collatz_general), run_time=6)
        self.wait(6)
        self.play(FadeOut(collatz_general))

        example1 = [12, 6, 3, 10, 5, 16, 8, 4, 2, 1]
        example_tex = []
        example_arrows = []

        for n in example1:
            print(n)
            example_tex.append(MathTex(n))

        example_tex[0].to_edge(LEFT * 2).shift(DOWN * 2).scale(1.4)
        
        for n in range(1, len(example_tex)):
            example_tex[n].next_to(example_tex[n-1], RIGHT * 4).scale(1.4)
            example_arrows.append(Arrow(start=example_tex[n-1].get_right(), end=example_tex[n].get_left()))
        
        self.play(Write(example_tex[0]))
        self.wait(5)

        for n in range(1, len(example_tex)):
            self.play(Write(example_tex[n]), Create(example_arrows[n-1]), run_time=1.4)

        curved = CurvedArrow(example_tex[9].get_top() + (UP * 0.2), example_tex[7].get_top() + (UP * 0.2))

        self.play(Create(curved))
        self.wait(20)

class ConjectureVsTheorem(Scene):
    def construct(self):
        question = Text("What is a conjecture?", t2c={' a conject':YELLOW})
        question.scale(1.5)
        self.play(Write(question))
        self.wait(17)

        math_conjecture = Text("Mathematical Conjecture", color=YELLOW)
        math_conjecture.scale(1.5)
        self.play(ReplacementTransform(question, math_conjecture))
        self.play(math_conjecture.animate.shift(UP))

        explanation1 = Text("An educated guess about \nmathematical objects.").next_to(math_conjecture, direction=DOWN * 2, aligned_edge=LEFT)
        explanation2 = Text("A proposition which you believe to be true, \nbut have no proof of.").next_to(math_conjecture, direction=DOWN * 2, aligned_edge=LEFT)
        self.play(Write(explanation1))
        self.wait(1)
        self.play(ReplacementTransform(explanation1, explanation2))
        self.wait(8)


        math_theorem = Text("Theorem", color=YELLOW)
        math_theorem.scale(1.5).move_to(math_conjecture, aligned_edge=LEFT)

        explanation3 = Text("A proposition which has been proven \nthrough the methods of mathematical \nproof.").next_to(math_conjecture, direction=DOWN * 2, aligned_edge=LEFT)
        self.play(ReplacementTransform(explanation2, explanation3), ReplacementTransform(math_conjecture, math_theorem))
        self.wait(3)

        conjecture = Text("Conjecture", color=YELLOW)
        conjecture.scale(1.5).move_to(math_theorem, aligned_edge=LEFT)

        self.play(FadeOut(explanation3))
        example = Text("Every natural number is either \neven or odd.").next_to(math_theorem, direction=DOWN * 2, aligned_edge=LEFT)
        self.wait(3)
        self.play(Write(example))
        self.wait(4)
        self.play(ReplacementTransform(math_theorem, conjecture))
        self.wait(22)
        self.play(FadeOut(example), FadeOut(conjecture))

class CollatzDifficulty(Scene): 
    def construct(self):
        collatz = Text("Collatz Conjecture", color=YELLOW).scale(1.5).shift(UP)
        fact = Text("Has been obseved to be true upto \nabout 300, 000, 000, 000, 000, 000!")
        fact.next_to(collatz, direction=DOWN * 2, aligned_edge = LEFT)

        self.play(Write(collatz))
        self.wait(14)
        self.play(Write(fact))
        self.wait(14)

        self.play(collatz.animate.scale(0.75).to_corner(UL).set_color(WHITE), FadeOut(fact))

        difficult = Text("Why is it so difficult to prove?").scale(1.2).shift(DOWN * 0.5)
        self.play(Write(difficult))
        self.wait(33)
        self.play(FadeOut(difficult))

class ModifiedExplanation(Scene):
    def construct(self):
        title = Text("Collatz Conjecture").to_corner(UL)
        self.add(title)

        collatz_left = MathTex(
            r"f(", r"n", r") = \begin{cases} \\ \\ \\ \end{cases}"
        ).shift(LEFT * 2)

        collatz_even_eq = MathTex(
            r"\frac{n}{2}"
        ).shift(UP * 0.5)

        collatz_odd_eq = MathTex(
            r"n + 1"
        ).shift(DOWN * 0.5)

        collatz_even = MathTex(
            r"\text{if $n \equiv 0$ (mod 2)}"
        ).next_to(collatz_even_eq, RIGHT * 7)

        collatz_odd = MathTex(
            r"\text{if $n \equiv 1$ (mod 2)}"
        ).next_to(collatz_even, direction=DOWN * 2.2, aligned_edge=LEFT)

        collatz_right = Group(collatz_even_eq, collatz_odd_eq, collatz_odd, collatz_even)

        collatz_right.next_to(collatz_left, RIGHT)

        collatz_equation = Group(collatz_left, collatz_right)

        self.wait(4)
        self.play(Write(collatz_left[0]), Write(collatz_left[2]))
        self.wait(7)
        self.play(Write(collatz_left[1]), Write(collatz_odd))
        self.wait(2)
        self.play(Write(collatz_odd_eq))

        collatz_example = MathTex("f(", "15", ") = ", "n + 1 = ", "16")
        collatz_example.next_to(collatz_odd_eq, direction=DOWN * 6)

        self.play(Write(collatz_example[0]), Write(collatz_example[2]))
        self.play(Write(collatz_example[1]), Indicate(collatz_left[1]))
        self.play(Write(collatz_example[3:]), Indicate(collatz_odd_eq))

        self.wait(3)
        self.play(Write(collatz_even), FadeOut(collatz_example))
        self.wait(2)
        self.play(Write(collatz_even_eq))

        collatz_example1 = MathTex("f(", "16", ") = ", r"\frac{n}{2} = ", "8")
        collatz_example1.next_to(collatz_odd_eq, direction=DOWN * 6)

        self.play(Write(collatz_example1[0]), Write(collatz_example1[2]))
        self.play(Write(collatz_example1[1]), Indicate(collatz_left[1]))
        self.play(Write(collatz_example1[3:]), Indicate(collatz_even_eq))

        self.play(FadeOut(collatz_example1))

        self.play(collatz_equation.animate.shift(UP))
        self.wait(2)

        example1 = [11, 12, 6, 3, 4, 2, 1]
        example_tex = []
        example_arrows = []

        for n in example1:
            print(n)
            example_tex.append(MathTex(n))

        example_tex[0].to_edge(LEFT * 3).shift(DOWN * 2).scale(1.4)
        
        for n in range(1, len(example_tex)):
            example_tex[n].next_to(example_tex[n-1], RIGHT * 6).scale(1.4)
            example_arrows.append(Arrow(start=example_tex[n-1].get_right(), end=example_tex[n].get_left()))
        
        self.play(Write(example_tex[0]))
        self.wait()

        for n in range(1, len(example_tex)):
            self.play(Write(example_tex[n]), Create(example_arrows[n-1]), run_time=1.3)

        self.wait(14)

class SimpleProof(Scene):
    def construct(self):
        title = Text("Collatz Conjecture").to_corner(UL)
        self.add(title)

        line1 = Tex(r"Suppose ", r"$n$", r" is odd").next_to(title, DOWN * 2, aligned_edge=LEFT)
        line1r = Tex(r"$n \equiv 1 \text{ (mod 2)}$").next_to(line1, RIGHT * 15)

        line2 = Tex(r"$n + 1$", " is even")
        line2[0].next_to(line1[1], DOWN * 4)
        line2[1].next_to(line2[0], RIGHT)
        line2r = Tex(r"$n \equiv 0 \text{ (mod 2)}$").next_to(line1r, DOWN, aligned_edge=LEFT).match_y(line2)

        arrow1 = Arrow(start=line1[1].get_bottom(), end=line2[0].get_top())

        line3 = MathTex(r"\frac{n+1}{2}").next_to(line2[0], DOWN * 4)
        line3r = MathTex(r"\frac{n}{2} + \frac{1}{2}", " < n")
        line3r[0].next_to(line2[0], DOWN * 4)
        line3r[1].next_to(line3r[0], RIGHT)

        arrow2 = Arrow(start=line2[0].get_bottom(), end=line3[0].get_top())

        self.play(Write(line1), run_time=2)
        self.play(Write(line1r))
        self.wait(2)
        self.play(Create(arrow1), Write(line2[0]))
        self.wait(2)
        self.play(Write(line2[1]),Write(line2r))
        self.wait(1)
        self.play(Create(arrow2), Write(line3))
        self.wait(5)
        self.play(ReplacementTransform(line3, line3r[0]))
        self.wait(1)
        self.play(Write(line3r[1]))

        example1 = [11, 12, 6, 3, 4, 2, 1]
        example_tex = []
        example_arrows = []
        all_fade_in = []

        for n in example1:
            print(n)
            example_tex.append(MathTex(n))

        example_tex[0].to_edge(LEFT * 3).shift(DOWN * 2.2).scale(1.4)
        
        for n in range(1, len(example_tex)):
            example_tex[n].next_to(example_tex[n-1], RIGHT * 6).scale(1.4)
            example_arrows.append(Arrow(start=example_tex[n-1].get_right(), end=example_tex[n].get_left()))         
        
        for n in example_tex: 
            all_fade_in.append(FadeIn(n))

        for n in example_arrows:
            all_fade_in.append(FadeIn(n))

        b1 = BraceBetweenPoints(example_tex[0].get_left() + (DOWN * 0.2), example_tex[2].get_right() + (DOWN * 0.2))
        b2 = BraceBetweenPoints(example_tex[3].get_left() + (DOWN * 0.2), example_tex[5].get_right() + (DOWN * 0.2))
        t1 = b1.get_text("Always smaller!").scale(0.9)
        t2 = b2.get_text("Always smaller!").scale(0.9)

        self.wait(2)
        self.play(*all_fade_in)
        self.wait(3)
        self.play(Create(b1), Write(t1))
        self.wait(2)
        self.play(ReplacementTransform(b1, b2), ReplacementTransform(t1, t2))
        self.wait(5)

class BasicCollatzProof(Scene):
    def construct(self):
        title = Text("Collatz Conjecture").to_corner(UL)
        self.add(title)

        line1 = Tex(r"Suppose ", r"$n$", r" is odd").next_to(title, DOWN * 2, aligned_edge=LEFT)
        line1r = Tex(r"$n \equiv 1 \text{ (mod 2)}$").next_to(line1, RIGHT * 15)

        line2 = Tex(r"$3n + 1$", " is even")
        line2[0].next_to(line1[1], DOWN * 4)
        line2[1].next_to(line2[0], RIGHT)
        line2r = Tex(r"$n \equiv 0 \text{ (mod 2)}$").next_to(line1r, DOWN, aligned_edge=LEFT).match_y(line2)

        arrow1 = Arrow(start=line1[1].get_bottom(), end=line2[0].get_top())

        line3 = MathTex(r"\frac{3n+1}{2}").next_to(line2[0], DOWN * 4)
        line3r = MathTex(r"\frac{3n}{2} + \frac{1}{2}", r" \nless n")
        line3r[0].next_to(line2[0], DOWN * 4)
        line3r[1].next_to(line3r[0], RIGHT)

        arrow2 = Arrow(start=line2[0].get_bottom(), end=line3[0].get_top())

        self.play(Write(line1), run_time=2)
        self.play(Write(line1r))
        self.wait(4)
        self.play(Create(arrow1), Write(line2[0]))
        self.wait(2)
        self.play(Write(line2[1]), Write(line2r))
        self.wait(1)
        self.play(Create(arrow2), Write(line3))
        self.wait(2)
        self.play(ReplacementTransform(line3, line3r[0]))
        self.wait(1)
        self.play(Write(line3r[1]))

        example1 = [12, 6, 3, 10, 5, 16, 8, 4, 2, 1]
        example_tex = []
        example_arrows = []
        all_fade_in = []

        for n in example1:
            print(n)
            example_tex.append(MathTex(n))

        example_tex[0].to_edge(LEFT * 2).shift(DOWN * 2).scale(1.4)
        
        for n in range(1, len(example_tex)):
            example_tex[n].next_to(example_tex[n-1], RIGHT * 4).scale(1.4)
            example_arrows.append(Arrow(start=example_tex[n-1].get_right(), end=example_tex[n].get_left()))

        for n in example_tex: 
            all_fade_in.append(FadeIn(n))

        for n in example_arrows:
            all_fade_in.append(FadeIn(n))

        b1 = BraceBetweenPoints(example_tex[1].get_left() + (DOWN * 0.2), example_tex[3].get_right() + (DOWN * 0.2))
        b2 = BraceBetweenPoints(example_tex[3].get_left() + (DOWN * 0.2), example_tex[5].get_right() + (DOWN * 0.2))
        t1 = b1.get_text("Not smaller!").scale(0.9)
        t2 = b2.get_text("Not smaller!").scale(0.9)

        self.wait(2)
        self.play(*all_fade_in)
        self.wait(3)
        self.play(Create(b1), Write(t1))
        self.wait(2)
        self.play(ReplacementTransform(b1, b2), ReplacementTransform(t1, t2))
        self.wait(5)
        

class CollatzHeuristic(Scene):
    def construct(self):
        title = Text("Collatz Conjecture").to_corner(UL)
        self.add(title)

        lagarias_image = ImageMobject("assets/jeff_lagarias.jpg").scale(2.5).next_to(title, DOWN, aligned_edge=LEFT)
        lagarias_name = Text("Jeffrey Lagarias").scale(0.9).next_to(lagarias_image, DOWN)

        line1 = MathTex(r"n_0 \rightarrow n_{1}").next_to(lagarias_image, RIGHT * 2.5, aligned_edge=UP).shift(DOWN * 0.2)
        line1r = MathTex(r"n_x \equiv 1 \text{ (mod 2)}").next_to(line1, RIGHT * 5)

        line2 = MathTex(r"P\left(n_{1} = \frac{3n_0 + 1}{2}\right) = \frac{1}{2}").next_to(line1, DOWN * 2.5, aligned_edge=LEFT)

        line3 = MathTex(r"P\left(n_{1} = \frac{3n_0 + 1}{4}\right) = \frac{1}{4}").next_to(line2, DOWN * 2.5, aligned_edge=LEFT)

        line4 = MathTex(r"P\left(n_{1} = \frac{3n_0 + 1}{8}\right) = \frac{1}{8}").next_to(line3, DOWN * 2.5, aligned_edge=LEFT)


        self.wait(11)
        self.play(FadeIn(lagarias_image), Write(lagarias_name))
        self.wait(3)
        self.play(Write(line1))
        self.play(Write(line1r))
        self.wait(4)
        self.play(Write(line2))
        self.wait(7)
        self.play(Write(line3))
        self.wait(5)
        self.play(Write(line4))
        self.wait(20)
        self.play(FadeOut(lagarias_image), FadeOut(lagarias_name), FadeOut(line1), FadeOut(line1r), FadeOut(line2), FadeOut(line3), FadeOut(line4))

class TaoPaper(Scene):
    def construct(self):
        title = Text("Collatz Conjecture").to_corner(UL)
        self.add(title)

        korec_paper = Tex("A density estimate for the $3x+ 1$ problem")
        korec_name = Tex("$\sim$ Ivan Korec, 1994").scale(0.9).next_to(korec_paper, DOWN, aligned_edge=RIGHT)
        
        korec_group = Group(korec_name, korec_paper)

        korec_discovery = MathTex("f(n) < n^{0.7925}").shift(DOWN)

        self.wait(8)
        self.play(Write(korec_paper), Write(korec_name))
        self.wait(1)
        self.play(korec_group.animate.shift(UP))
        self.wait(1)
        self.play(Write(korec_discovery))
        self.wait(5)

        self.play(FadeOut(korec_group), FadeOut(korec_discovery))

        tao_image = ImageMobject("assets/tao..jpg").scale(0.43).next_to(title, DOWN, aligned_edge=LEFT)
        tao_name = Text("Terence Tao").scale(0.9).next_to(tao_image, DOWN)

        tao_group = Group(tao_image, tao_name)

        tao_paper = Tex("Almost all orbits of the Collatz map \n\nattain almost bounded values").next_to(tao_group, RIGHT * 3)
        tao_credit = Tex("$\sim$ Terence Tao, 2019").scale(0.9).next_to(tao_paper, DOWN, aligned_edge=RIGHT)

        tao_paper_group = Group(tao_paper, tao_credit)
        
        self.play(FadeIn(tao_image), Write(tao_name))
        self.wait(15)
        self.play(Write(tao_paper), Write(tao_credit)) 
        self.wait(20)

        self.play(tao_paper_group.animate.shift(UP * 2))

        odd = MathTex(r"n \equiv 1 \text{ (mod 2)}").next_to(tao_paper_group, DOWN * 5)
        factors_of_three = MathTex(r"n \equiv 0 \text{ (mod 3)}").next_to(odd, DOWN * 2)
        cross = Cross(factors_of_three, stroke_color=RED)
        not_factors_of_three = MathTex(r"n \equiv 1 \text{ (mod 3)}").next_to(odd, DOWN * 2)

        self.wait(4)
        self.play(Write(odd))
        self.play(Write(factors_of_three))

        self.wait(22)
        self.play(FadeOut(odd))
        self.play(Create(cross))
        self.play(FadeOut(factors_of_three), FadeOut(cross))
        self.play(Write(not_factors_of_three))
        self.wait(10)
        self.play(FadeOut(not_factors_of_three))

        conclusion = Text("Almost all numbers produce a number close \nto 1 after going through many Collatz \nsequences")
        conclusion.scale(0.65).next_to(tao_paper_group, DOWN * 4)
        self.play(Write(conclusion))
        self.wait(12)
        self.play(FadeOut(tao_group), FadeOut(tao_paper_group), FadeOut(conclusion))

class WhyCollatz(Scene):
    def construct(self):
        title = Text("Collatz Conjecture").to_corner(UL)
        self.add(title)

        erdos_image = ImageMobject("assets/Erdos_budapest_fall_1992_(cropped).jpg")
        erdos_image.to_edge(LEFT).scale(1.75).shift(RIGHT)
        erdos_name = Text("Paul Erdős")
        erdos_name.scale(0.95).next_to(erdos_image, DOWN)

        erdos_group = Group(erdos_image, erdos_name)

        self.wait(10)
        self.play(FadeIn(erdos_image), Write(erdos_name))

        bounty_amount = Text("$500!", color=YELLOW).scale(2).match_y(erdos_group).shift(RIGHT * 2)

        self.wait(9)
        self.play(Write(bounty_amount))
        self.wait(2)
        self.play(FadeOut(erdos_group), FadeOut(bounty_amount))

        vertices = [1, 2, 3, 4]
        edges = [(1, 2), (2, 3), (3, 4), (1, 3), (1, 4)]

        graph = Graph(vertices, edges).scale(0.8).shift(LEFT * 3)
        graph_text = Text("Graph Theory").scale(0.8).next_to(graph, DOWN * 2)
        number = MathTex("2n + 1").scale(3).shift(RIGHT * 3)
        number_text = Text("Number Theory").scale(0.8).next_to(number, DOWN).match_y(graph_text)

        number_group = Group(number, number_text)
        graph_group = Group(graph, graph_text)

        self.wait(12)
        self.play(Create(graph), Write(graph_text))
        self.play(Create(number), Write(number_text))
        self.wait(20)

        self.play(FadeOut(number_group), FadeOut(graph_group))

        perhaps = Text("Perhaps there exists some use for \nthe Collatz Conjecture")

        self.wait(5)
        self.play(Write(perhaps))
        self.wait(13)
        self.play(FadeOut(perhaps))

        self.wait(6)
        grid = NumberPlane()
        self.play(Create(grid))
        self.wait(12)
        self.play(ApplyWave(grid, amplitude=1))
        self.play(FadeOut(grid), FadeOut(title))

        visualization = ImageMobject("assets/collatz_visualization.png").scale(0.5).shift(UP * 0.5)
        self.play(FadeIn(visualization))
        self.wait(26)
        self.play(FadeOut(visualization))

        we_discussed = Text("We discussed:").to_edge(LEFT).shift(UP)
        techniques = Text("Techniques of Mathematical Proofs").scale(1.2).next_to(we_discussed, DOWN, aligned_edge=LEFT)
        moduli = Text("Moduli").scale(1.2).next_to(techniques, DOWN, aligned_edge=LEFT)
        random_variables = Text("Random Variables").scale(1.2).next_to(moduli, DOWN, aligned_edge=LEFT)

        discussed_group = Group(we_discussed, techniques, moduli, random_variables)

        self.wait(15)
        self.play(Write(we_discussed))
        self.play(Write(techniques))
        self.play(Write(moduli))
        self.play(Write(random_variables))
        self.wait(16)
        self.play(FadeOut(discussed_group))

        thanks = Text("Thank you!", color=YELLOW).scale(1.5)

        self.wait(2)
        self.play(Write(thanks))
        self.wait(7)
        self.play(FadeOut(thanks))

class Credits(Scene):
    def construct(self):
        title = Text("Credits").scale(1.1)
        title.to_corner(UL)

        self.play(Write(title))
        
        music = Text("Music by Vincent Rubinetti").scale(0.9).next_to(title, DOWN * 2, aligned_edge=LEFT)
        self.play(Write(music))

        collatz = Text("Lothar Collatz Photograph by Konrad Jacobs").scale(0.9).next_to(music, DOWN, aligned_edge=LEFT)
        self.play(Write(collatz))

        kakutani = Text("Shizou Kakutani Photograph by Konrad Jacobs").scale(0.9).next_to(collatz, DOWN, aligned_edge=LEFT)
        self.play(Write(kakutani))

        erdos = Text("Paul Erdős Photograph by Kmhkmh").scale(0.9).next_to(kakutani, DOWN, aligned_edge=LEFT)
        self.play(Write(erdos))

        leingang = Text("Matthew Leingang Photograph: Courtesy NYU Courant").scale(0.9).next_to(erdos, DOWN, aligned_edge=LEFT)
        self.play(Write(leingang))

        lagarias = Text("Jeffery Lagarias Photograph from his site").scale(0.9).next_to(leingang, DOWN, aligned_edge=LEFT)
        self.play(Write(lagarias))

        tao = Text("Terence Tao Photograph: Courtesy UCLA").scale(0.9).next_to(lagarias, DOWN, aligned_edge=LEFT)
        self.play(Write(tao))

        self.wait(10)
        
