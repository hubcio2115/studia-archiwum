package lab4

type Pred[A] = A => Boolean

def and[A](p: Pred[A], q: Pred[A]): Pred[A] = {
  (x: A) => p(x) && q(x)
}

def or[A](p: Pred[A], q: Pred[A]): Pred[A] = {
  (x: A) => p(x) || q(x)
}

def not[A](p: Pred[A]): Pred[A] = {
  (x: A) => !p(x)
}

def imp[A](p: Pred[A], q: Pred[A]): Pred[A] = {
  (x: A) => !p(x) || q(x)
}
