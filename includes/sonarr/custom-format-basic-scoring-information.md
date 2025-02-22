<!-- markdownlint-disable MD041-->
!!! info "How Does Custom Format Scoring Work?"

    Let’s say you have three custom formats, A, B and C. Scored as:

        A: 10
        B: 20
        C: 30

    Then, let’s say you have three releases, X, Y and Z. They happen to match your custom formats as follows:

        X matches A
        Y matches B and C
        Z matches A and C

    Total custom format scores would therefore be:

        X: 10 (matches A)
        Y: 50 (matches B and C)
        Z: 40 (matches A and C)

    Quality is the first check. If all three of our example releases here are the same quality - eg, WEBDL-1080p, then we move on to the next check which is custom format score. In the example above, Y would be chosen as it has the highest cumulative custom format score.
<!-- markdownlint-enable MD041-->
