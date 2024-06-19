/**
 * v0 by Vercel.
 * @see https://v0.dev/t/17OnA7ibTpJ
 * Documentation: https://v0.dev/docs#integrating-generated-code-into-your-nextjs-app
 */
import Link from "next/link"

export default function Component() {
  return (
    <section className="w-full py-12 md:py-24 lg:py-32 xl:py-48">
      <div className="container px-4 md:px-6">
        <div className="grid gap-6 lg:grid-cols-[1fr_600px] lg:gap-12 xl:grid-cols-[1fr_800px]">
          <img
            src="/placeholder.svg"
            width="800"
            height="600"
            alt="Hero"
            className="mx-auto aspect-[4/3] overflow-hidden rounded-xl object-cover sm:w-full lg:order-last"
          />
          <div className="flex flex-col justify-center space-y-4">
            <div className="space-y-2">
              <h1 className="text-3xl font-bold tracking-tighter sm:text-5xl xl:text-6xl/none">
                Discover the Latest Fashion Trends
              </h1>
              <p className="max-w-[600px] text-gray-500 md:text-xl dark:text-gray-400">
                Explore our curated collection of stylish and high-quality apparel, accessories, and more. Find the
                perfect pieces to elevate your wardrobe.
              </p>
            </div>
            <div className="flex flex-col gap-2 min-[400px]:flex-row">
              <Link
                href="#"
                className="inline-flex h-10 items-center justify-center rounded-md bg-gray-900 px-8 text-sm font-medium text-gray-50 shadow transition-colors hover:bg-gray-900/90 focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-gray-950 disabled:pointer-events-none disabled:opacity-50 dark:bg-gray-50 dark:text-gray-900 dark:hover:bg-gray-50/90 dark:focus-visible:ring-gray-300"
                prefetch={false}
              >
                Shop Now
              </Link>
            </div>
          </div>
        </div>
      </div>
    </section>
  )
}