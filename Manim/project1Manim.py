from manim import *
config.pixel_height = 1080
config.pixel_width = 1920
config.frame_rate = 60

class ProblemOne(ThreeDScene):
    def surfaceOne(self, u, v):
        return np.array([u, v, 1 + v])

    def surfaceTwo(self, u, v):
        return np.array([u, v, np.sqrt(u ** 2 + v ** 2)])

    def surfaceThree(self, u, v):
        return np.array([u, v, (2.5 * u) - v - 0.5])

    def surfaceFour(self, u, v):
        return np.array([u, v, 6.0 - (4.0 * u) - v])


    def construct(self):
        axes = ThreeDAxes()

        x_label = axes.get_x_axis_label(Tex("x"))
        y_label = axes.get_y_axis_label(Tex("y"))
        z_label = axes.get_z_axis_label(Tex("z"))
        # .shift(UP * 1.8)

        l1 = Text("Problem 1").to_edge(DL)
        # l2 = Text("Problem 2").to_edge(DL)
        # l3 = Text("Problem 3").to_edge(DL)
        eq1 = Tex("$z=1+y$").to_edge(DR)
        eq2 = Tex("$z=\sqrt{x^2+y^2}$").to_edge(DR)
        eq3 = MathTex(r'\vec{r}(t)=<t,\frac{1}{2}t^2-\frac{1}{2},\frac{1}{2}t^2+\frac{1}{2}>',font_size=36).to_edge(DR)
        eq4 = Tex("$5x-2y-2z=1$").to_edge(DR)
        eq5 = Tex("$4x+y+z=6$").to_edge(DR)

        # zoom out so we see the axes
        self.set_camera_orientation(zoom=0.3)

        self.play(FadeIn(axes), FadeIn(x_label), FadeIn(y_label), FadeIn(z_label))

        self.wait(0.5)

        # animate the move of the camera to properly see the axes
        self.move_camera(phi=75 * DEGREES, theta=30 * DEGREES, zoom=0.6, run_time=1.5)

        surface1 = Surface(
            lambda u, v: axes.c2p(*self.surfaceOne(u, v)),
            u_range=[-5, 5],
            v_range=[-5, 5],
            resolution=8,
        )

        surface2 = Surface(
            lambda u, v: axes.c2p(*self.surfaceTwo(u, v)),
            u_range=[-5, 5],
            v_range=[-5, 5],
            resolution=8,
        )

        surface3 = Surface(
            lambda u, v: axes.c2p(*self.surfaceThree(u, v)),
            u_range=[-2, 2],
            v_range=[-2, 2],
            resolution=10,
        )

        surface4 = Surface(
            lambda u, v: axes.c2p(*self.surfaceFour(u, v)),
            u_range=[-2, 
            2],
            v_range=[-2, 2],
            resolution=10,
        )

        curve1 = ParametricFunction(
            lambda u: np.array([
                u,
                (1/2) * (u ** 2) - (1 / 2),
                (1/2) * (u ** 2) + (1 / 2)
            ]), color=RED, t_range = np.array([-10, 10, 0.01])
        ).set_shade_in_3d(True)

        curve2 = ParametricFunction(
            lambda u: np.array([
                1,
                2 + (-13.0 * u),
                (13.0 * u)
            ]), color=RED, t_range = np.array([-10, 10, 0.01])
        ).set_shade_in_3d(True)

        surface1.set_color(BLUE)
        surface2.set_color(ORANGE)
        surface3.set_color(BLUE)
        surface4.set_color(ORANGE)

        self.begin_ambient_camera_rotation(rate=0.15)
        self.add_fixed_in_frame_mobjects(l1)
        self.play(Write(l1))
        self.wait(2)
        self.play(FadeIn(surface1))
        self.add_fixed_in_frame_mobjects(eq1)
        self.play(Write(eq1))
        # built-in updater which begins camera rotation
        self.wait(3)
        self.play(FadeOut(eq1,shift=DOWN))
        self.play(FadeOut(surface1))
        self.play(FadeIn(surface2))
        self.add_fixed_in_frame_mobjects(eq2)
        self.play(Write(eq2))
        self.wait(3)
        self.play(FadeOut(eq2,shift=DOWN))
        self.play(FadeOut(surface2))
        # fade in space curve
        self.add_fixed_in_frame_mobjects(eq3)
        self.play(Write(eq3))
        self.play(FadeIn(curve1))
        self.wait(3)
        self.play(FadeIn(surface1))
        self.play(FadeIn(surface2))
        self.wait(3)
        self.play(surface1.animate.set_opacity(0.3))
        self.play(surface2.animate.set_opacity(0.3))
        self.wait(3)
        self.play(FadeOut(VGroup(l1, eq3, surface1, surface2, curve1)))
        # self.add_fixed_in_frame_mobjects(l2)
        # self.play(Write(l2))
        # self.wait(2)
        # self.play(FadeIn(surface3))
        # self.add_fixed_in_frame_mobjects(eq4)
        # self.play(Write(eq4))
        # self.wait(3)
        # self.play(FadeOut(surface3))
        # self.play(FadeOut(eq4))
        # self.play(FadeIn(surface4))
        # self.add_fixed_in_frame_mobjects(eq5)
        # self.play(Write(eq5))
        # self.wait(3)
        # self.play(FadeOut(eq5,shift=DOWN))
        # self.play(FadeIn(surface3))
        # self.wait(3)
        # self.play(FadeIn(curve2))
        # self.wait(5)
