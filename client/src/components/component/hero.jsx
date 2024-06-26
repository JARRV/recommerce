/**
 * v0 by Vercel.
 * @see https://v0.dev/t/dIkeQXrErC7
 * Documentation: https://v0.dev/docs#integrating-generated-code-into-your-nextjs-app
 */
// import Link from "next/link";

export default function Component() {
  return (
    <section className="relative w-full h-[80vh] min-h-[500px] flex items-center justify-center bg-gray-900 overflow-hidden">
      <img
        src="/placeholder.svg"
        alt="Hero Background"
        className="absolute inset-0 w-full h-full object-cover opacity-50"
      />
      <div className="relative z-10 text-center max-w-3xl px-4 sm:px-6 lg:px-8">
        <h1 className="text-4xl font-extrabold tracking-tight text-white sm:text-5xl lg:text-6xl">
          Discover the Best Products
        </h1>
        <p className="mt-3 text-xl text-gray-300 sm:mt-5 sm:text-2xl lg:text-3xl">
          Browse our curated collection of high-quality products for your home,
          office, and lifestyle.
        </p>
        <div className="mt-10 sm:mt-12">
          <Link
            href="#"
            className="inline-flex items-center justify-center px-8 py-3 border border-transparent text-base font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 md:py-4 md:text-lg md:px-10"
            prefetch={false}
          >
            Shop Now
          </Link>
        </div>
      </div>
    </section>
  );
}
