### Bad path suggestion

!!! warning "The default path setup suggested by some docker developers that encourages people to use mounts like `/movies`, `/tv`, `/books` or `/downloads` is very suboptimal and it makes them look like two or three file systems, even if they aren’t (_Because of how Docker’s volumes work_). It is the easiest way to get started. While easy to use, it has a major drawback. Mainly losing the ability to hardlink or instant move, resulting in a slower and more I/O intensive copy + delete is used."
